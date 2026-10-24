"""`leet next` picks a due review first, then the next new problem."""
import datetime

import pytest

from leet import cli, progress

D = datetime.date


@pytest.fixture
def progress_file(tmp_path, monkeypatch):
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    return progress.PATH


def run_next(capsys, *argv):
    args = cli.build_parser().parse_args(["next", *argv])
    try:
        args.func(args)
    except SystemExit as exc:
        return str(exc.code), capsys.readouterr().out
    return None, capsys.readouterr().out


def test_next_suggests_a_due_review_before_new_problems(progress_file, capsys):
    progress.record("003-two-sum", True, today=D(2020, 1, 1))
    _, out = run_next(capsys)
    assert "due for review" in out and "Two Sum" in out and "leet start 3" in out


def test_next_with_nothing_due_suggests_the_first_unsolved(progress_file, capsys):
    today = datetime.date.today()
    progress.record("001-contains-duplicate", True, today=today)
    _, out = run_next(capsys)
    assert "Next problem in roadmap order" in out and "Valid Anagram" in out


def test_next_new_skips_reviews(progress_file, capsys):
    progress.record("001-contains-duplicate", True, today=D(2020, 1, 1))
    _, out = run_next(capsys, "--new")
    assert "due for review" not in out and "Contains Duplicate" not in out
