"""Every reference solution comes with a written explanation."""
import pytest

from leet.problems import all_problems


@pytest.mark.parametrize("problem", all_problems(), ids=lambda p: p.key)
def test_has_an_explanation(problem):
    text = problem.load_explanation()
    assert text, "missing explanation.md"
    assert text.startswith("### Approach"), "start with an Approach section"
    assert "### Complexity" in text, "include a Complexity section"
    assert "<" not in text.replace("<=", "").replace("<<", ""), "plain markdown only, no HTML"
