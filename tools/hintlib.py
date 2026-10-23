"""Attach tiered hints to problem folders.

Each tools/hints/<category>.py defines HINTS = {problem_id: [hint1, hint2, hint3]}.
For a hinted problem this writes hints.json and replaces the README's plain
"Hints" section with a collapsed <details> block (so statements don't spoil the
solution; the web UI hides that block and reveals hints one at a time instead).
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

TIERS = 3


def load_hints():
    import hints as pkg

    out = {}
    for info in pkgutil.iter_modules(pkg.__path__):
        mod = importlib.import_module(f"hints.{info.name}")
        for pid, tiers in mod.HINTS.items():
            if pid in out:
                raise SystemExit(f"duplicate hints for problem {pid}")
            out[pid] = tiers
    return out


def apply(folder, tiers):
    if len(tiers) != TIERS or not all(isinstance(t, str) and t.strip() for t in tiers):
        raise SystemExit(f"{folder.name}: expected exactly {TIERS} non-empty hints")
    (folder / "hints.json").write_text(json.dumps(tiers, indent=2, ensure_ascii=False) + "\n")
    readme = folder / "README.md"
    text = readme.read_text()
    cuts = [i for i in (text.find("\n## Hints"), text.find("\n<details>")) if i != -1]
    if cuts:
        text = text[: min(cuts)]
    items = "\n".join(f"{n}. {t}" for n, t in enumerate(tiers, 1))
    readme.write_text(
        f"{text.rstrip()}\n\n<details>\n<summary>Hints (spoilers: open one at a time)</summary>\n\n{items}\n\n</details>\n"
    )


def apply_all():
    hints = load_hints()
    folders = {p.id: p.dir for p in all_problems()}
    for pid, tiers in sorted(hints.items()):
        if pid not in folders:
            raise SystemExit(f"hints given for unknown problem {pid}")
        apply(folders[pid], tiers)
    return len(hints)


def missing():
    hints = load_hints()
    return [p for p in all_problems() if p.difficulty != "Easy" and p.id not in hints]


if __name__ == "__main__":
    n = apply_all()
    left = missing()
    print(f"applied hints to {n} problems; {len(left)} Medium/Hard without hints")
    for p in left:
        print(f"  {p.id} {p.title}")
