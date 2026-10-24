import argparse
import shutil
import subprocess
import sys

from leet import progress
from leet import perf
from leet.execute import all_passed, run_perf, run_problem
from leet.problems import all_problems, find
from leet.reset import reset


def _resolve(query):
    if query is None:
        query = progress.load()["current"]
        if query is None:
            sys.exit("no problem given and none started yet; try `leet start <id>`")
    try:
        return find(query)
    except LookupError as exc:
        sys.exit(str(exc))


def _fmt(value):
    text = repr(value)
    return text if len(text) <= 200 else text[:197] + "..."


def _print_results(problem, outcome):
    if "load_error" in outcome:
        print(f"{problem.title}: could not run\n{outcome['load_error']}")
        return False
    results = outcome["results"]
    passed = sum(r["ok"] for r in results)
    print(f"{problem.title} ({problem.difficulty})  {passed}/{len(results)} passed")
    for i, r in enumerate(results, 1):
        print(f"  {'PASS' if r['ok'] else 'FAIL'}  case {i}")
    first_fail = next((r for r in results if not r["ok"]), None)
    if first_fail:
        print("\nFirst failure:")
        print(f"  input:    {_fmt(first_fail['args'])}")
        print(f"  expected: {_fmt(first_fail['expected'])}")
        if "error" in first_fail:
            print(f"  error:\n{first_fail['error']}")
        else:
            print(f"  got:      {_fmt(first_fail['got'])}")
        if first_fail["stdout"]:
            print(f"  stdout:\n{first_fail['stdout']}")
    return passed == len(results) and _print_hidden(outcome.get("hidden"))


def _print_hidden(hidden):
    """Print the hidden-test result. Returns True when there is nothing to fail."""
    if hidden is None or hidden.get("skipped"):
        return True
    if "error" in hidden:
        print(f"\nHidden tests could not run:\n{hidden['error']}")
        return False
    failure = hidden.get("failure")
    if not failure:
        print(f"Hidden tests: {hidden['passed']}/{hidden['total']} passed")
        return True
    print(f"\nHidden tests: failed {failure['case']} of {hidden['total']} (input about {failure['input_size']:,} characters)")
    if failure["error"]:
        print(f"  error: {failure['error'].strip().splitlines()[-1]}")
    else:
        print(f"  expected: {failure['expected']}\n  got:      {failure['got']}")
    if failure["error"] == "time limit exceeded":
        print("  Your solution passes the visible tests but is too slow for large inputs.")
    return False


def cmd_list(args):
    for p in all_problems():
        if args.category and args.category != p.category:
            continue
        status = progress.status(p.key)
        if args.todo and status == "solved":
            continue
        if args.hidden and not p.hidden:
            continue
        print(f"{p.id:>3}  {status:<9}  {p.difficulty:<6}  {p.category:<16}  {p.title}")


def cmd_start(args):
    problem = _resolve(args.problem)
    progress.set_current(problem.key)
    editor = shutil.which("code")
    if editor:
        subprocess.run([editor, str(problem.readme_path), str(problem.solution_path)])
    else:
        print("`code` not on PATH; open these in VS Code:")
    print(f"  {problem.readme_path}\n  {problem.solution_path}")


def cmd_test(args):
    problem = _resolve(args.problem)
    progress.set_current(problem.key)
    ok = _print_results(problem, run_problem(problem))
    progress.record(problem.key, ok)
    sys.exit(0 if ok else 1)


def cmd_reset(args):
    problem = _resolve(args.problem)
    if not args.yes:
        if not sys.stdin.isatty():
            sys.exit("pass --yes to reset without a prompt")
        answer = input(f"Replace your solution to {problem.title} with the starter code? A backup is kept. [y/N] ")
        if answer.strip().lower() not in ("y", "yes"):
            sys.exit("not reset")
    backup = reset(problem)
    print(f"{problem.title}: solution.py is back to the starter code")
    if backup:
        print(f"your previous code is saved in {backup.relative_to(problem.dir.parents[2])}")


def cmd_perf(args):
    problem = _resolve(args.problem)
    print(f"{problem.title} ({problem.difficulty})")
    report = run_perf(problem)
    print(perf.format_report(report))
    sys.exit(1 if "error" in report else 0)


def cmd_validate(args):
    problems = [_resolve(args.problem)] if args.problem else all_problems()
    failed = 0
    for p in problems:
        if not p.reference_path.exists():
            print(f"MISSING  {p.key}: no reference solution")
            failed += 1
            continue
        outcome = run_problem(p, reference=True)
        results = outcome.get("results")
        if not all_passed(outcome):
            failed += 1
            print(f"FAIL     {p.key}")
            _print_results(p, outcome)
        else:
            extra = f" + {outcome['hidden']['total']} hidden" if "hidden" in outcome else ""
            print(f"ok       {p.key}  ({len(results)} cases{extra})")
    sys.exit(1 if failed else 0)


def cmd_serve(args):
    from leet.server import serve

    serve(port=args.port, open_browser=not args.no_open)


def main():
    parser = argparse.ArgumentParser(prog="leet")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("list", help="list problems with status")
    p.add_argument("--category")
    p.add_argument("--todo", action="store_true", help="hide solved problems")
    p.add_argument("--hidden", action="store_true", help="only problems that have hidden tests")
    p.set_defaults(func=cmd_list)

    for name, func, help_ in [
        ("start", cmd_start, "open a problem in VS Code"),
        ("test", cmd_test, "run a problem's tests against solution.py"),
    ]:
        p = sub.add_parser(name, help=help_)
        p.add_argument("problem", nargs="?", help="id, slug, or a path inside the problem")
        p.set_defaults(func=func)

    p = sub.add_parser("reset", help="restore a problem's starter code (your code is backed up first)")
    p.add_argument("problem", nargs="?", help="id, slug, or a path inside the problem")
    p.add_argument("-y", "--yes", action="store_true", help="do not ask for confirmation")
    p.set_defaults(func=cmd_reset)

    p = sub.add_parser("perf", help="compare your passing solution's speed and memory with the reference")
    p.add_argument("problem", nargs="?", help="id, slug, or a path inside the problem")
    p.set_defaults(func=cmd_perf)

    p = sub.add_parser("validate", help="run reference solutions against the tests")
    p.add_argument("problem", nargs="?")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("serve", help="start the local web UI")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--no-open", action="store_true", help="don't open the browser")
    p.set_defaults(func=cmd_serve)

    args = parser.parse_args()
    args.func(args)
