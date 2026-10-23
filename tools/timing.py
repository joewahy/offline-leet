"""Run each spec's brute-force solution against the full tests.json with a short time limit.

Shows which problems have large cases that a naive solution cannot pass.

    python tools/timing.py [spec-module ...]
"""
import dataclasses
import importlib
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from build import CATEGORIES, slugify  # noqa: E402
from leet import problems as P_  # noqa: E402
from leet.runner import load_checker, load_module, run_case  # noqa: E402

LIMIT = 2.0


def main(argv):
    for name in argv or CATEGORIES:
        module = importlib.import_module(f"specs.{name}")
        for spec in module.PROBLEMS:
            if "brute" not in spec:
                continue
            key = f"{spec['id']:03d}-{slugify(spec['title'])}"
            problem = dataclasses.replace(P_._load(ROOT / "problems" / module.CATEGORY / key / "meta.json"), timeout=LIMIT)
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "brute.py"
                path.write_text(spec["brute"])
                brute = load_module(path, problem)
                checker = load_checker(problem)
                cases = problem.load_cases()
                passed = timeouts = 0
                for case in cases:
                    r = run_case(problem, brute, checker, case)
                    passed += r["ok"]
                    if r.get("error") == "time limit exceeded":
                        timeouts += 1
                        break
                wrong = len(cases) - passed - timeouts
            verdict = "naive solution times out" if timeouts else ("naive solution passes all" if wrong == 0 else "brute FAILS")
            print(f"{key:<58} {verdict}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
