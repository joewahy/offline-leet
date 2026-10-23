"""Attach target time and space complexity to each problem's meta.json.

Each tools/complexity_data/<category>.py defines
COMPLEXITY = {problem_id: (time, space)}, for example (`"O(n)"`, `"O(1)"`).
The target is what a good solution should achieve, shown next to the
performance comparison. build.py re-applies it after every build.

    python tools/complexity.py     apply to every problem and list any without one
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
    import complexity_data as pkg

    out = {}
    for info in pkgutil.iter_modules(pkg.__path__):
        mod = importlib.import_module(f"complexity_data.{info.name}")
        for pid, (time, space) in mod.COMPLEXITY.items():
            if pid in out:
                raise SystemExit(f"duplicate complexity for problem {pid}")
            out[pid] = {"time": time, "space": space}
    return out


def apply_all():
    data = load_data()
    folders = {p.id: p.dir for p in all_problems()}
    for pid, target in sorted(data.items()):
        if pid not in folders:
            raise SystemExit(f"complexity given for unknown problem {pid}")
        path = folders[pid] / "meta.json"
        meta = json.loads(path.read_text())
        meta["complexity"] = target
        path.write_text(json.dumps(meta) + "\n")
    return len(data)


def missing():
    data = load_data()
    return [p for p in all_problems() if p.id not in data]


if __name__ == "__main__":
    n = apply_all()
    left = missing()
    print(f"applied complexity to {n} problems; {len(left)} without one")
    for p in left:
        print(f"  {p.id} {p.title}")
