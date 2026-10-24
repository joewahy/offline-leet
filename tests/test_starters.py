"""Every problem ships a starter.py that loads and defines what the tests call."""
import contextlib
import io

import pytest

from leet.problems import all_problems
from leet.runner import load_module


@pytest.mark.parametrize("problem", all_problems(), ids=lambda p: p.key)
def test_starter_loads(problem):
    assert problem.starter_path.exists(), "missing starter.py (run tools/build.py)"
    with contextlib.redirect_stdout(io.StringIO()):
        module = load_module(problem.starter_path, problem)
    name = problem.design or (problem.roundtrip or {}).get("class") or "Solution"
    assert hasattr(module, name), f"starter.py does not define {name}"
