"""Attach hidden tests to problems.

Each tools/hidden_data/<category>.py defines HIDDEN = {problem_id: (constraints, source)}.

  source       the text of the problem's hidden.py: generate(rng) returns a list of
               argument lists. They are built when the tests run (expected values come
               from the reference solution), so no big files are stored in git.
  constraints  [(old, new)] edits to the README's Constraints list, so that the
               statement allows the sizes the hidden tests use.

build.py re-applies this after every build.

    python tools/hiddenlib.py     apply to every problem and list those that have hidden tests
"""
import importlib
import json
import pkgutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from leet.problems import all_problems  # noqa: E402


def load_data():
    import hidden_data as pkg

    out = {}
    for info in pkgutil.iter_modules(pkg.__path__):
        mod = importlib.import_module(f"hidden_data.{info.name}")
        for pid, entry in mod.HIDDEN.items():
            if pid in out:
                raise SystemExit(f"duplicate hidden tests for problem {pid}")
            out[pid] = entry
    return out


def edit_readme(problem, edits):
    path = problem.readme_path
    text = path.read_text()
    for old, new in edits:
        if text.count(old) == 1:
            text = text.replace(old, new)
        elif text.count(new) != 1:
            raise SystemExit(f"{problem.key}: constraint {old!r} not found in README.md")
    path.write_text(text)


def apply_all():
    data = load_data()
    problems = {p.id: p for p in all_problems()}
    for pid in data:
        if pid not in problems:
            raise SystemExit(f"hidden tests given for unknown problem {pid}")
    for pid, problem in problems.items():
        meta_path = problem.dir / "meta.json"
        meta = json.loads(meta_path.read_text())
        if pid not in data:
            if meta.pop("hidden", None) is not None:
                meta_path.write_text(json.dumps(meta) + "\n")
            problem.hidden_path.unlink(missing_ok=True)
            continue
        constraints, source = data[pid]
        edit_readme(problem, constraints)
        problem.hidden_path.write_text(source.strip("\n") + "\n")
        meta["hidden"] = True
        meta_path.write_text(json.dumps(meta) + "\n")
    return len(data)


if __name__ == "__main__":
    print(f"applied hidden tests to {apply_all()} problems")
