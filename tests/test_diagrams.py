"""Diagram images that the statements link to."""
import sys

import pytest

from leet.problems import ROOT, all_problems

sys.path.insert(0, str(ROOT / "tools"))
import diagrams  # noqa: E402


@pytest.mark.parametrize("problem", all_problems(), ids=lambda p: p.key)
def test_readme_links_a_diagram_exactly_when_the_file_exists(problem):
    linked = diagrams.LINK in problem.readme_path.read_text()
    assert linked == (problem.dir / "diagram.svg").exists()


@pytest.mark.parametrize("problem", [p for p in all_problems() if (p.dir / "diagram.svg").exists()], ids=lambda p: p.key)
def test_diagram_matches_what_the_generator_draws(problem):
    assert (problem.dir / "diagram.svg").read_text() == diagrams.render(
        diagrams.blocks(problem), f"Diagram of example 1 of {problem.title}"
    )


def test_linking_is_idempotent():
    readme = "# 1. X (Easy)\n\n## Examples\n\n```\nInput: a\n```\n\n## Constraints\n"
    once = diagrams.link(readme)
    assert once.count(diagrams.LINK) == 1
    assert diagrams.link(once) == once
