"""The performance comparison against the reference solution."""
import pytest

from leet import perf
from leet.problems import find

# Longest Consecutive Sequence: the reference runs in a couple of milliseconds
# on its biggest cases, which makes the ratios below stable.
PROBLEM = "009"

REPEATED = '''
class Solution:
    def longestConsecutive(self, nums):
        for _ in range(60):
            s = set(nums)
            best = 0
            for x in s:
                if x - 1 not in s:
                    y = x
                    while y + 1 in s:
                        y += 1
                    best = max(best, y - x + 1)
        return best
'''

HUNGRY = '''
class Solution:
    def longestConsecutive(self, nums):
        junk = [0] * 3_000_000
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                y = x
                while y + 1 in s:
                    y += 1
                best = max(best, y - x + 1)
        return best + len(junk) * 0
'''


@pytest.fixture
def problem():
    return find(PROBLEM)


def write(tmp_path, source):
    path = tmp_path / "solution.py"
    path.write_text(source)
    return str(path)


def test_reference_against_itself_is_on_par(problem):
    report = perf.measure(problem, str(problem.reference_path))
    assert "error" not in report
    assert report["time"]["verdict"] in ("faster", "similar")
    assert report["time"]["ratio"] < 4
    assert report["memory"]["verdict"] == "similar"
    assert 1 <= len(report["cases"]) <= perf.TOP_CASES
    assert report["target"] == problem.complexity


def test_solution_that_fails_tests_is_not_measured(problem):
    report = perf.measure(problem)  # the untouched starter stub
    assert "does not pass all the tests" in report["error"]


def test_much_slower_solution_is_flagged(problem, tmp_path):
    report = perf.measure(problem, write(tmp_path, REPEATED))
    assert "error" not in report
    assert report["time"]["verdict"] == "much_slower"
    assert report["time"]["ratio"] > 8


def test_memory_hungry_solution_is_flagged(problem, tmp_path):
    report = perf.measure(problem, write(tmp_path, HUNGRY))
    assert "error" not in report
    assert report["memory"]["verdict"] == "much_more"


def row(time, ref_time, timed_out=False, memory=None, ref_memory=None):
    return {
        "time": time,
        "ref_time": ref_time,
        "time_ratio": max(time, perf.TIME_FLOOR) / max(ref_time, perf.TIME_FLOOR),
        "timed_out": timed_out,
        "memory": memory,
        "ref_memory": ref_memory,
        "memory_ratio": None if memory is None else max(memory, perf.MEMORY_FLOOR) / max(ref_memory, perf.MEMORY_FLOOR),
    }


@pytest.mark.parametrize(
    "rows, expected",
    [
        ([row(0.1, 0.1)], "similar"),
        ([row(0.05, 0.1)], "faster"),
        ([row(0.4, 0.1)], "slower"),
        ([row(2.0, 0.1)], "much_slower"),
        ([row(5.0, 0.1, timed_out=True)], "timeout"),
        ([row(0.0001, 0.0002)], "too_small"),
    ],
)
def test_time_verdicts(rows, expected):
    assert perf.time_verdict(rows)[0] == expected


@pytest.mark.parametrize(
    "rows, expected",
    [
        ([row(0.1, 0.1, memory=1_000_000, ref_memory=1_000_000)], "similar"),
        ([row(0.1, 0.1, memory=400_000, ref_memory=1_000_000)], "less"),
        ([row(0.1, 0.1, memory=5_000_000, ref_memory=1_000_000)], "more"),
        ([row(0.1, 0.1, memory=50_000_000, ref_memory=1_000_000)], "much_more"),
        ([row(0.1, 0.1, memory=1000, ref_memory=2000)], "too_small"),
    ],
)
def test_memory_verdicts(rows, expected):
    assert perf.memory_verdict(rows)[0] == expected
