"""Add larger generated cases to problems 1-5.

Those five were written by hand before the build pipeline existed, so they have
no spec in tools/specs/. This keeps their hand-written cases and appends big
ones (expected values come from the reference solution), which the performance
comparison needs. Safe to re-run: it always starts from the hand-written cases.

    python tools/extend_basic_cases.py
"""
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from build import write_tests  # noqa: E402
from leet.compare import matches, norm  # noqa: E402
from leet.problems import find  # noqa: E402
from leet.runner import execute, load_module  # noqa: E402

HAND_CASES = {1: 7, 2: 8, 3: 8, 4: 7, 5: 7}


def _letters(rng, n, alphabet="abcdefghijklmnopqrstuvwxyz"):
    return "".join(rng.choice(alphabet) for _ in range(n))


def contains_duplicate(rng):
    distinct = rng.sample(range(-10 ** 9, 10 ** 9), 10000)
    with_dup = distinct[:-1] + [distinct[len(distinct) // 3]]
    return [[distinct], [with_dup]]


def valid_anagram(rng):
    a = _letters(rng, 50000)
    shuffled = list(a)
    rng.shuffle(shuffled)
    b = "".join(shuffled)
    off_by_one = b[:-1] + ("a" if b[-1] != "a" else "b")
    return [[a, b], [a, off_by_one]]


def two_sum(rng):
    return []


def group_anagrams(rng):
    bases = [_letters(rng, 100) for _ in range(100)]
    words = []
    for _ in range(1000):
        letters = list(rng.choice(bases))
        rng.shuffle(letters)
        words.append("".join(letters))
    return [[words]]


def top_k(rng):
    out = []
    while len(out) < 2:
        nums = [rng.randint(-1000, 1000) for _ in range(10000)]
        counts = sorted((nums.count(v) for v in set(nums)), reverse=True)
        k = rng.choice([1, 3, 10])
        if counts[k - 1] > counts[k]:
            out.append([nums, k])
    return [out[0], out[1]]


GENERATORS = {1: contains_duplicate, 2: valid_anagram, 3: two_sum, 4: group_anagrams, 5: top_k}


def main():
    for pid, generate in GENERATORS.items():
        problem = find(str(pid))
        module = load_module(problem.reference_path, problem)
        hand = [(c["args"], c["expected"]) for c in problem.load_cases()[: HAND_CASES[pid]]]
        extra = []
        for args in generate(random.Random(pid)):
            got, _, _ = execute(problem, module, args)
            extra.append((args, norm(got)))
        write_tests(problem.dir / "tests.json", hand + extra)
        print(f"{problem.key}: {len(hand)} hand + {len(extra)} generated")


if __name__ == "__main__":
    main()
