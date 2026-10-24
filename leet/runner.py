"""Runs one problem's cases in a child process and prints JSON results.

Usage: python -m leet.runner <problem-dir-name> [--reference]
"""
import contextlib
import copy
import importlib.util
import io
import json
import signal
import sys
import traceback

from leet import hidden, memguard, structures
from leet.compare import matches, norm
from leet.problems import find

sys.setrecursionlimit(10000)

STOP_ERRORS = ("time limit exceeded", "memory limit exceeded")


def _on_alarm(signum, frame):
    raise TimeoutError("time limit exceeded")


def load_module(path, problem):
    """Import a solution file with NeetCode's predefined names already in scope."""
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    module.__dict__.update(structures.prelude(problem.arg_types))
    spec.loader.exec_module(module)
    return module


def load_checker(problem):
    if not problem.checker:
        return None
    spec = importlib.util.spec_from_file_location("check", problem.checker_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.check


def prepare(problem, module, args):
    """Decode one case. Returns (call, finish).

    call() does only the solution's work and returns its raw result, so it can
    be timed on its own. finish(raw) turns that into (encoded result, raw
    result, decoded inputs).
    """
    args = copy.deepcopy(args)

    if problem.design:
        ops, params = args

        def call():
            cls = getattr(module, problem.design)
            instance, out = None, []
            for i, (op, p) in enumerate(zip(ops, params)):
                if i == 0:
                    instance = cls(*p)
                    out.append(None)
                else:
                    out.append(getattr(instance, op)(*p))
            return out

        return call, lambda out: (out, out, [])

    if problem.roundtrip:
        rt = problem.roundtrip
        value = structures.decode(rt["type"], args[0], [])

        def call():
            cls = getattr(module, rt["class"])
            data = getattr(cls(), rt["encode"])(value)
            if not isinstance(data, str):
                raise TypeError(f"{rt['encode']} must return a str, got {type(data).__name__}")
            return getattr(cls(), rt["decode"])(data)

        return call, lambda back: (structures.encode(rt["type"], back), back, [value])

    types = problem.arg_types or ("plain",) * len(args)
    decoded = []
    for kind, value in zip(types, args):
        decoded.append(structures.decode(kind, value, decoded))
    inputs = list(decoded)
    method = getattr(module.Solution(), problem.method)

    def finish(returned):
        if problem.inplace is not None:
            i = problem.inplace
            return structures.encode(types[i], decoded[i]), decoded[i], inputs
        return structures.encode(problem.return_type, returned), returned, inputs

    return (lambda: method(*decoded)), finish


def execute(problem, module, args):
    """Run one case. Returns (encoded result, raw result, decoded inputs)."""
    call, finish = prepare(problem, module, args)
    return finish(call())


def check_case(problem, checker, case, got, raw, inputs, result):
    if checker:
        verdict = checker(case["args"], raw, case["expected"], inputs)
        if isinstance(verdict, str):
            result["error"] = verdict
        return verdict is True
    return matches(problem.compare, got, case["expected"])


def run_case(problem, module, checker, case):
    result = {"args": case["args"], "expected": case["expected"], "stdout": ""}
    buf = io.StringIO()
    signal.signal(signal.SIGALRM, _on_alarm)
    signal.setitimer(signal.ITIMER_REAL, problem.timeout)
    try:
        with contextlib.redirect_stdout(buf), memguard.guard():
            got, raw, inputs = execute(problem, module, case["args"])
            got = norm(got)
            result["got"] = got
            result["ok"] = check_case(problem, checker, case, got, raw, inputs, result)
    except BaseException as exc:
        result["ok"] = False
        result["error"] = (
            str(exc)
            if isinstance(exc, (TimeoutError, memguard.MemoryLimitExceeded))
            else traceback.format_exc(limit=-3)
        )
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    result["stdout"] = buf.getvalue()
    return result


def hidden_cases(problem):
    """The hidden cases, from the cache or generated with the reference solution."""
    cases = hidden.load_cached(problem)
    if cases is not None:
        return cases
    with contextlib.redirect_stdout(io.StringIO()):
        reference = load_module(problem.reference_path, problem)
        cases = []
        for args in hidden.generate_args(problem):
            got, _, _ = execute(problem, reference, args)
            cases.append({"args": args, "expected": norm(got)})
    hidden.store(problem, cases)
    return cases


def run_hidden(problem, module, checker):
    """Run the hidden cases until one fails. Never returns the inputs, which are huge."""
    try:
        cases = hidden_cases(problem)
    except BaseException:
        return {"error": traceback.format_exc(limit=-3)}
    summary = {"total": len(cases), "passed": 0}
    for number, case in enumerate(cases, 1):
        result = run_case(problem, module, checker, case)
        if result["ok"]:
            summary["passed"] += 1
            continue
        summary["failure"] = {
            "case": number,
            "input_size": len(json.dumps(case["args"])),
            "error": result.get("error"),
            "expected": hidden.shorten(case["expected"]),
            "got": hidden.shorten(result.get("got")),
            "stdout": result["stdout"][:500],
        }
        break
    return summary


def main(argv):
    memguard.start()
    problem = find(argv[0])
    path = problem.reference_path if "--reference" in argv else problem.solution_path
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            module = load_module(path, problem)
            checker = load_checker(problem)
    except BaseException:
        print(json.dumps({"load_error": traceback.format_exc(limit=-3)}))
        return
    results = []
    stopped = False
    for case in problem.load_cases():
        if stopped:
            results.append({**case, "ok": False, "got": None, "stdout": "",
                            "error": "skipped after an earlier timeout or memory error"})
            continue
        result = run_case(problem, module, checker, case)
        stopped = result.get("error", "").startswith(STOP_ERRORS)
        results.append(result)
    outcome = {"results": results}
    if problem.hidden:
        if all(r["ok"] for r in results):
            outcome["hidden"] = run_hidden(problem, module, checker)
        else:
            outcome["hidden"] = {"skipped": True}
    print(json.dumps(outcome, default=repr))


if __name__ == "__main__":
    main(sys.argv[1:])
