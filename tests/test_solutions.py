"""Shows every case of every problem in VS Code's Testing panel.

Run one problem with: pytest tests -k two-sum
"""
from functools import lru_cache

import pytest

from leet.execute import run_problem
from leet.problems import all_problems


@lru_cache(maxsize=None)
def _outcome(key):
    problem = next(p for p in all_problems() if p.key == key)
    return run_problem(problem)


PARAMS = [
    pytest.param(p.key, i, id=f"{p.key}-case{i + 1}")
    for p in all_problems()
    for i in range(len(p.load_cases()))
]


@pytest.mark.parametrize("key,index", PARAMS)
def test_case(key, index):
    outcome = _outcome(key)
    assert "load_error" not in outcome, outcome.get("load_error")
    result = outcome["results"][index]
    assert result["ok"], (
        f"input={result['args']!r} expected={result['expected']!r} "
        f"got={result.get('got')!r}\n{result.get('error', '')}"
    )
