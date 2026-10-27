"""Hidden tests: generated on demand, cached, and reported without the inputs."""
import dataclasses
import json
import time
import types

import pytest

from leet import hidden, runner
from leet.problems import find

KEY = "009-longest-consecutive-sequence"
HIDDEN_PY = """
def generate(rng):
    return [[list(range(50000))], [[rng.randint(0, 10**9) for _ in range(3)]]]
"""


@pytest.fixture
def problem(tmp_path, monkeypatch):
    """Problem 9 with its hidden.py and cache redirected to a temp folder."""
    folder = tmp_path / KEY
    folder.mkdir()
    (folder / "hidden.py").write_text(HIDDEN_PY)
    monkeypatch.setattr(hidden, "CACHE_DIR", tmp_path / "cache")
    return dataclasses.replace(find("009"), dir=folder, hidden=True, timeout=0.5)


def solution(body):
    namespace = {}
    exec(f"class Solution:\n    def longestConsecutive(self, nums):\n{body}", {"time": time}, namespace)
    return types.SimpleNamespace(Solution=namespace["Solution"])


def test_cases_are_generated_with_reference_answers(problem):
    cases = runner.hidden_cases(problem)
    assert len(cases) == 2
    assert cases[0]["expected"] == 50000


def test_second_call_reads_the_cache(problem, monkeypatch):
    runner.hidden_cases(problem)
    monkeypatch.setattr(hidden, "generate_args", lambda p: pytest.fail("regenerated"))
    assert len(runner.hidden_cases(problem)) == 2


def test_cache_is_rebuilt_when_hidden_py_changes(problem):
    runner.hidden_cases(problem)
    problem.hidden_path.write_text(HIDDEN_PY.replace("50000", "10"))
    assert runner.hidden_cases(problem)[0]["expected"] == 10


def test_corrupt_cache_is_ignored(problem):
    runner.hidden_cases(problem)
    hidden.cache_path(problem).write_text("{ nope")
    assert runner.hidden_cases(problem)[0]["expected"] == 50000


def test_correct_solution_passes_all(problem):
    ref = runner.load_module(problem.reference_path, problem)
    assert runner.run_hidden(problem, ref, None) == {"total": 2, "passed": 2}


def test_wrong_answer_is_reported_without_the_input(problem):
    summary = runner.run_hidden(problem, solution("        return 0"), None)
    failure = summary["failure"]
    assert (summary["passed"], failure["case"]) == (0, 1)
    assert failure["input_size"] > 100000
    assert failure["expected"] == "50000" and failure["got"] == "0"
    assert "args" not in failure and len(json.dumps(summary)) < 1000


def test_slow_solution_times_out(problem):
    summary = runner.run_hidden(problem, solution("        time.sleep(2)\n        return 0"), None)
    assert summary["failure"]["error"] == "time limit exceeded"


def test_broken_hidden_py_is_an_error_not_a_crash(problem):
    problem.hidden_path.write_text("def generate(rng):\n    raise RuntimeError('boom')\n")
    summary = runner.run_hidden(problem, solution("        return 0"), None)
    assert "boom" in summary["error"]


def test_every_hidden_problem_has_a_generator_and_no_other_does():
    from leet.problems import all_problems

    for p in all_problems():
        assert p.hidden == p.hidden_path.exists(), f"{p.key}: meta.json and hidden.py disagree"
        if p.hidden:
            source = p.hidden_path.read_text()
            assert "def generate(rng)" in source, p.key


def test_hidden_problems_state_the_size_the_tests_use():
    import re

    from leet.problems import all_problems

    for p in all_problems():
        if p.hidden and "constraints are unchanged" not in p.hidden_path.read_text():
            assert re.search(r"10\^5|100000|\d \* 10\^4", p.readme_path.read_text()), (
                f"{p.key}: README constraints do not allow the hidden tests' size"
            )
