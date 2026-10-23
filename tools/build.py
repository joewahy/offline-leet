"""Materialise problem specs into problems/, reference/, and tests.json files.

    python tools/build.py              build every spec
    python tools/build.py two_pointers build one spec module (tools/specs/<name>.py)

Per problem this:
  1. writes meta.json, README.md, solution.py (only if missing), reference/<key>.py
  2. checks the reference against the hand-written cases
  3. generates extra cases (expected values come from the reference)
  4. cross-checks the reference against a brute-force solution on small random inputs
  5. writes tests.json
"""
import importlib
import json
import random
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from leet import problems as P_  # noqa: E402
from leet.compare import matches, norm  # noqa: E402
from leet.runner import execute, load_checker, load_module, run_case  # noqa: E402

CATEGORIES = [
    "arrays_hashing", "two_pointers", "sliding_window", "stack", "binary_search",
    "linked_list", "trees", "heap", "backtracking", "tries", "graphs",
    "advanced_graphs", "dp_1d", "dp_2d", "greedy", "intervals", "math_geometry",
    "bit_manipulation",
]
META_OPTS = ["compare", "timeout", "arg_types", "return_type", "inplace", "design", "roundtrip"]


def slugify(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def write_tests(path, cases):
    lines = [json.dumps({"args": a, "expected": e}, separators=(", ", ": ")) for a, e in cases]
    path.write_text("[\n  " + ",\n  ".join(lines) + "\n]\n")


def build(spec, category):
    key = f"{spec['id']:03d}-{slugify(spec['title'])}"
    folder = ROOT / "problems" / category / key
    folder.mkdir(parents=True, exist_ok=True)

    meta = {k: spec[k] for k in ("id", "title") if k in spec}
    meta.update(category=category, difficulty=spec["difficulty"], method=spec["method"])
    for k in META_OPTS:
        if k in spec:
            meta[k] = spec[k]
    if spec.get("checker"):
        meta["checker"] = True
        (folder / "check.py").write_text(spec["checker"].strip() + "\n")
    (folder / "meta.json").write_text(json.dumps(meta) + "\n")
    (folder / "README.md").write_text(
        f"# {spec['id']}. {spec['title']} ({spec['difficulty']})\n\n{spec['statement'].strip()}\n"
    )
    if not (folder / "solution.py").exists():
        (folder / "solution.py").write_text(spec["stub"].strip("\n") + "\n")
    ref_path = ROOT / "reference" / f"{key}.py"
    ref_path.write_text(spec["reference"].strip("\n") + "\n")

    hand = [(a, e) for a, e in spec["cases"]]
    write_tests(folder / "tests.json", hand)
    problem = P_._load(folder / "meta.json")
    module = load_module(ref_path, problem)
    checker = load_checker(problem)

    for i, (args, expected) in enumerate(hand, 1):
        r = run_case(problem, module, checker, {"args": args, "expected": expected})
        if not r["ok"]:
            raise SystemExit(
                f"{key}: reference fails hand case {i}\n  args:     {args!r:.300}\n"
                f"  expected: {expected!r:.300}\n  got:      {r.get('got')!r:.300}\n"
                f"  error:    {r.get('error', '')}"
            )

    rng = random.Random(spec["id"])
    extra = []
    if "gen" in spec:
        for args in spec["gen"](rng):
            got, raw, inputs = execute(problem, module, args)
            extra.append((args, norm(got)))
    for args, expected in extra:
        r = run_case(problem, module, checker, {"args": args, "expected": expected})
        if not r["ok"]:
            raise SystemExit(f"{key}: reference fails its own generated case\n{r.get('error', '')}")

    checked = 0
    if "brute" in spec:
        with tempfile.TemporaryDirectory() as tmp:
            brute_path = Path(tmp) / "brute.py"
            brute_path.write_text(spec["brute"].strip("\n") + "\n")
            brute = load_module(brute_path, problem)
            for _ in range(spec.get("brute_runs", 60)):
                args = spec["small"](rng)
                ref_got, _, _ = execute(problem, module, args)
                bru_got, bru_raw, bru_inputs = execute(problem, brute, args)
                ref_got, bru_got = norm(ref_got), norm(bru_got)
                if checker:
                    ok = checker(args, bru_raw, ref_got, bru_inputs) is True
                else:
                    ok = matches(problem.compare, bru_got, ref_got)
                if not ok:
                    raise SystemExit(
                        f"{key}: reference and brute force disagree\n  args: {args!r:.300}\n"
                        f"  reference: {ref_got!r:.300}\n  brute:     {bru_got!r:.300}"
                    )
                checked += 1

    write_tests(folder / "tests.json", hand + extra)
    size = (folder / "tests.json").stat().st_size // 1024
    print(f"ok  {key:<55} hand={len(hand):<3} gen={len(extra):<3} brute={checked:<3} {size}KB")


def main(argv):
    names = [] if argv == ["--hints-only"] else (argv or CATEGORIES)
    for name in names:
        try:
            module = importlib.import_module(f"specs.{name}")
        except ModuleNotFoundError as exc:
            if exc.name == f"specs.{name}":
                print(f"-- skipping {name} (no spec yet)")
                continue
            raise
        for spec in module.PROBLEMS:
            build(spec, module.CATEGORY)
    import hintlib

    hintlib.apply_all()


if __name__ == "__main__":
    main(sys.argv[1:])
