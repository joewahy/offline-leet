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

from leet.compare import matches
from leet.problems import find


def _on_alarm(signum, frame):
    raise TimeoutError("time limit exceeded")


def _load_solution(path):
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_case(method, mode, timeout, case):
    result = {"args": case["args"], "expected": case["expected"], "stdout": ""}
    buf = io.StringIO()
    signal.signal(signal.SIGALRM, _on_alarm)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        with contextlib.redirect_stdout(buf):
            got = method(*copy.deepcopy(case["args"]))
        result["got"] = got
        result["ok"] = matches(mode, got, case["expected"])
    except BaseException as exc:
        result["ok"] = False
        result["error"] = (
            str(exc) if isinstance(exc, TimeoutError) else traceback.format_exc(limit=-3)
        )
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    result["stdout"] = buf.getvalue()
    return result


def main(argv):
    problem = find(argv[0])
    path = problem.reference_path if "--reference" in argv else problem.solution_path
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            module = _load_solution(path)
        method = getattr(module.Solution(), problem.method)
    except BaseException:
        print(json.dumps({"load_error": traceback.format_exc(limit=-3)}))
        return
    results = []
    timed_out = False
    for case in problem.load_cases():
        if timed_out:
            results.append({**case, "ok": False, "got": None, "stdout": "",
                            "error": "skipped after an earlier timeout"})
            continue
        result = run_case(method, problem.compare, problem.timeout, case)
        timed_out = result.get("error") == "time limit exceeded"
        results.append(result)
    print(json.dumps({"results": results}, default=repr))


if __name__ == "__main__":
    main(sys.argv[1:])
