"""Compare a solution's speed and memory with the reference on the biggest test cases.

Usage: python -m leet.perf <problem> [solution-path]

Prints a JSON report. This is an estimate, not a proof: it measures a few
large inputs and compares them with the reference solution on the same
machine, so a large ratio hints at a worse complexity class.
"""
import contextlib
import gc
import io
import json
import signal
import sys
import time
import tracemalloc
import traceback

from leet import memguard
from leet.problems import find
from leet.runner import load_checker, load_module, prepare, run_case

TOP_CASES = 3
TIME_FLOOR = 0.0005  # seconds: below this, timer noise dominates
MEMORY_FLOOR = 64 * 1024  # bytes: below this, allocator noise dominates
STEADY_TIME = 0.05  # a first run at least this long is trusted as is
RELEVANT = 0.1  # skip cases the reference finishes in under this fraction of the heaviest

TIME_MESSAGES = {
    "faster": "Faster than the reference.",
    "similar": "About as fast as the reference.",
    "slower": "Somewhat slower than the reference.",
    "much_slower": "Much slower than the reference, which usually means a worse time complexity.",
    "timeout": "Ran out of time on a large input, which usually means a worse time complexity.",
    "too_small": "These inputs run too fast to compare timings.",
}
MEMORY_MESSAGES = {
    "less": "Uses less memory than the reference.",
    "similar": "Uses about as much memory as the reference.",
    "more": "Uses more memory than the reference.",
    "much_more": "Uses much more memory than the reference.",
    "too_small": "Memory use is too small to compare.",
}


def _on_alarm(signum, frame):
    raise TimeoutError("time limit exceeded")


@contextlib.contextmanager
def _limit(seconds):
    signal.signal(signal.SIGALRM, _on_alarm)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


def _run_once(problem, module, args, limit):
    call, _ = prepare(problem, module, args)
    gc.collect()
    gc.disable()
    try:
        with _limit(limit):
            start = time.perf_counter()
            call()
            return time.perf_counter() - start
    finally:
        gc.enable()


def measure_time(problem, module, args):
    """Seconds for one call of the solution. Returns (seconds, timed_out)."""
    try:
        first = _run_once(problem, module, args, problem.timeout)
        best = first
        if first < STEADY_TIME:
            for _ in range(4):
                best = min(best, _run_once(problem, module, args, problem.timeout))
    except TimeoutError:
        return problem.timeout, True
    return best, False


def peak_memory(problem, module, args, limit):
    """Peak extra bytes allocated during one call (the input itself is not counted)."""
    call, _ = prepare(problem, module, args)
    gc.collect()
    tracemalloc.start()
    try:
        base = tracemalloc.get_traced_memory()[0]
        tracemalloc.reset_peak()
        with _limit(limit):
            call()
        return max(tracemalloc.get_traced_memory()[1] - base, 0)
    finally:
        tracemalloc.stop()


def _ratio(value, reference, floor):
    return max(value, floor) / max(reference, floor)


def time_verdict(rows):
    if any(r["timed_out"] for r in rows):
        return "timeout", None
    if all(max(r["time"], r["ref_time"]) < TIME_FLOOR for r in rows):
        return "too_small", None
    worst = max(r["time_ratio"] for r in rows)
    if worst <= 0.8:
        return "faster", worst
    if worst <= 2.5:
        return "similar", worst
    if worst <= 8:
        return "slower", worst
    return "much_slower", worst


def memory_verdict(rows):
    rows = [r for r in rows if r["memory"] is not None]
    if not rows or all(max(r["memory"], r["ref_memory"]) < MEMORY_FLOOR for r in rows):
        return "too_small", None
    worst = max(r["memory_ratio"] for r in rows)
    if worst <= 0.6:
        return "less", worst
    if worst <= 3:
        return "similar", worst
    if worst <= 10:
        return "more", worst
    return "much_more", worst


def _heaviest(problem, reference, cases):
    """Indices of the cases that take the reference longest, in input order."""
    costs = []
    for i, case in enumerate(cases):
        costs.append((_run_once(problem, reference, case["args"], problem.timeout * 4), i))
    costs.sort(key=lambda c: (-c[0], c[1]))
    chosen = [c for c in costs[:TOP_CASES] if c[0] >= costs[0][0] * RELEVANT]
    return sorted(i for _, i in chosen)


def measure(problem, solution_path=None):
    path = solution_path or problem.solution_path
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            solution = load_module(path, problem)
            reference = load_module(problem.reference_path, problem)
            checker = load_checker(problem)
            cases = problem.load_cases()
            for case in cases:
                if not run_case(problem, solution, checker, case)["ok"]:
                    return {"error": "Your solution does not pass all the tests yet, so its speed was not measured."}
            rows = []
            for i in _heaviest(problem, reference, cases):
                args = cases[i]["args"]
                t, timed_out = measure_time(problem, solution, args)
                ref_t, _ = measure_time(problem, reference, args)
                row = {
                    "case": i + 1,
                    "input_bytes": len(json.dumps(args)),
                    "time": t,
                    "ref_time": ref_t,
                    "time_ratio": _ratio(t, ref_t, TIME_FLOOR),
                    "timed_out": timed_out,
                    "memory": None,
                    "ref_memory": None,
                    "memory_ratio": None,
                }
                if not timed_out:
                    limit = problem.timeout * 3
                    try:
                        row["memory"] = peak_memory(problem, solution, args, limit)
                        row["ref_memory"] = peak_memory(problem, reference, args, limit)
                        row["memory_ratio"] = _ratio(row["memory"], row["ref_memory"], MEMORY_FLOOR)
                    except TimeoutError:
                        pass
                rows.append(row)
                if timed_out:
                    break
    except BaseException:
        return {"error": traceback.format_exc(limit=-3)}

    t_code, t_worst = time_verdict(rows)
    m_code, m_worst = memory_verdict(rows)
    return {
        "target": problem.complexity,
        "cases": rows,
        "time": {"verdict": t_code, "ratio": t_worst, "message": TIME_MESSAGES[t_code]},
        "memory": {"verdict": m_code, "ratio": m_worst, "message": MEMORY_MESSAGES[m_code]},
    }


def format_seconds(seconds):
    if seconds < 0.001:
        return f"{seconds * 1e6:.0f} us"
    if seconds < 1:
        return f"{seconds * 1000:.1f} ms"
    return f"{seconds:.2f} s"


def format_bytes(count):
    if count < 1024:
        return f"{count} B"
    if count < 1024 * 1024:
        return f"{count / 1024:.0f} KB"
    return f"{count / 1024 / 1024:.1f} MB"


def format_report(report):
    """Plain-text version of a measure() report."""
    if "error" in report:
        return report["error"]
    lines = []
    target = report.get("target")
    if target:
        lines.append(f"Target:  {target['time']} time, {target['space']} space")
    worst = max(report["cases"], key=lambda r: r["time_ratio"])
    time_note = f"{report['time']['ratio']:.1f}x the reference" if report["time"]["ratio"] else ""
    lines.append(f"Time:    {report['time']['message']} {time_note}".rstrip())
    lines.append(f"Memory:  {report['memory']['message']}")
    lines.append("")
    count = len(report["cases"])
    lines.append(f"Heaviest {count} input{'s' if count != 1 else ''} (yours vs the reference):")
    for r in report["cases"]:
        mine = "timed out" if r["timed_out"] else format_seconds(r["time"])
        memory = "" if r["memory"] is None else f"   memory {format_bytes(r['memory'])} vs {format_bytes(r['ref_memory'])}"
        lines.append(f"  case {r['case']:>2}  input {format_bytes(r['input_bytes']):>7}   time {mine} vs {format_seconds(r['ref_time'])}{memory}")
    return "\n".join(lines)


def main(argv):
    memguard.start()
    problem = find(argv[0])
    print(json.dumps(measure(problem, argv[1] if len(argv) > 1 else None)))


if __name__ == "__main__":
    main(sys.argv[1:])
