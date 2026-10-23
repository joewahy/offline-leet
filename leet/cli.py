import argparse
import shutil
import subprocess
import sys

from leet import progress
from leet.execute import run_problem
from leet.problems import all_problems, find


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
    return passed == len(results)


def cmd_list(args):
    for p in all_problems():
        if args.category and args.category != p.category:
            continue
        status = progress.status(p.key)
        if args.todo and status == "solved":
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
        if results is None or not all(r["ok"] for r in results):
            failed += 1
            print(f"FAIL     {p.key}")
            _print_results(p, outcome)
        else:
            print(f"ok       {p.key}  ({len(results)} cases)")
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
    p.set_defaults(func=cmd_list)

    for name, func, help_ in [
        ("start", cmd_start, "open a problem in VS Code"),
        ("test", cmd_test, "run a problem's tests against solution.py"),
    ]:
        p = sub.add_parser(name, help=help_)
        p.add_argument("problem", nargs="?", help="id, slug, or a path inside the problem")
        p.set_defaults(func=func)

    p = sub.add_parser("validate", help="run reference solutions against the tests")
    p.add_argument("problem", nargs="?")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("serve", help="start the local web UI")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--no-open", action="store_true", help="don't open the browser")
    p.set_defaults(func=cmd_serve)

    args = parser.parse_args()
    args.func(args)
