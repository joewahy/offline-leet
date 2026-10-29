"""Spaced repetition: solved problems come back for review on a schedule."""
import datetime
import json

import pytest

from leet import progress

D = datetime.date


@pytest.fixture
def progress_file(tmp_path, monkeypatch):
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    return progress.PATH


def entry(key="p"):
    return progress.load()["problems"][key]


def test_first_solve_starts_in_box_one_due_tomorrow(progress_file):
    progress.record("p", True, today=D(2026, 1, 1))
    assert entry() == {
        "attempts": 1, "solved": True, "last_attempt": "2026-01-01",
        "solved_at": "2026-01-01", "box": 1, "due": "2026-01-02",
    }
    assert progress.due_reviews(D(2026, 1, 1)) == []
    assert progress.due_reviews(D(2026, 1, 2)) == ["p"]


def test_passing_a_due_review_moves_up_a_box(progress_file):
    progress.record("p", True, today=D(2026, 1, 1))
    progress.record("p", True, today=D(2026, 1, 2))
    assert (entry()["box"], entry()["due"]) == (2, "2026-01-05")
    progress.record("p", True, today=D(2026, 1, 5))
    assert (entry()["box"], entry()["due"]) == (3, "2026-01-12")


def test_rerunning_before_it_is_due_does_not_advance(progress_file):
    progress.record("p", True, today=D(2026, 1, 1))
    for _ in range(5):
        progress.record("p", True, today=D(2026, 1, 1))
    assert (entry()["box"], entry()["due"]) == (1, "2026-01-02")


def test_failing_a_due_review_resets_to_box_one(progress_file):
    for day in (1, 2, 5):
        progress.record("p", True, today=D(2026, 1, day))
    progress.record("p", False, today=D(2026, 1, 12))
    assert (entry()["box"], entry()["due"]) == (1, "2026-01-13")
    assert entry()["solved"]


def test_failing_before_it_is_due_changes_nothing(progress_file):
    progress.record("p", True, today=D(2026, 1, 1))
    progress.record("p", False, today=D(2026, 1, 1))
    assert (entry()["box"], entry()["due"]) == (1, "2026-01-02")


def test_box_is_capped_at_the_last_interval(progress_file):
    day = D(2026, 1, 1)
    progress.record("p", True, today=day)
    for _ in range(10):
        day += datetime.timedelta(days=60)
        progress.record("p", True, today=day)
    assert entry()["box"] == len(progress.REVIEW_DAYS)
    assert D.fromisoformat(entry()["due"]) == day + datetime.timedelta(days=30)


def test_unsolved_problems_are_never_due(progress_file):
    progress.record("p", False, today=D(2026, 1, 1))
    assert progress.due_reviews(D(2030, 1, 1)) == []
    assert progress.summary(D(2030, 1, 1)) == {"p": ("attempted", False)}


def test_problems_solved_before_tracking_are_due_now(progress_file):
    progress_file.write_text(json.dumps({"current": None, "problems": {"old": {"attempts": 2, "solved": True}}}))
    assert progress.due_reviews(D(2026, 1, 1)) == ["old"]
    progress.record("old", True, today=D(2026, 1, 1))
    assert (entry("old")["box"], entry("old")["due"]) == (2, "2026-01-04")


def test_longest_overdue_comes_first(progress_file):
    progress.record("a", True, today=D(2026, 1, 10))
    progress.record("b", True, today=D(2026, 1, 1))
    assert progress.due_reviews(D(2026, 2, 1)) == ["b", "a"]


def test_due_on_is_the_next_review_date_of_a_solved_problem(progress_file):
    assert progress.due_on("p") is None
    progress.record("p", False, today=D(2026, 1, 1))
    assert progress.due_on("p") is None
    progress.record("p", True, today=D(2026, 1, 1))
    assert progress.due_on("p") == "2026-01-02"


def test_reset_all_clears_progress_and_keeps_a_backup(progress_file, tmp_path):
    progress.record("p", True, today=D(2026, 1, 1))
    backup = progress.reset_all(backup_dir=tmp_path / "backups")
    assert progress.load() == {"current": None, "problems": {}}
    assert json.loads(backup.read_text())["problems"]["p"]["solved"] is True


def test_reset_all_without_a_progress_file_has_nothing_to_back_up(progress_file, tmp_path):
    assert progress.reset_all(backup_dir=tmp_path / "backups") is None
    assert progress.load() == {"current": None, "problems": {}}


def test_seconds_add_up_without_marking_the_problem_attempted(progress_file):
    assert progress.seconds("p") == 0
    assert progress.add_seconds("p", 30) == 30
    assert progress.add_seconds("p", 12.5) == 42.5
    assert progress.seconds("p") == 42.5
    assert progress.status("p") == "todo"
    assert progress.summary() == {}


def test_first_solve_records_the_time_spent_so_far(progress_file):
    progress.add_seconds("p", 90)
    progress.record("p", False, today=D(2026, 1, 1))
    assert progress.solve_seconds("p") is None
    progress.record("p", True, today=D(2026, 1, 1))
    progress.add_seconds("p", 500)
    progress.record("p", True, today=D(2026, 1, 2))
    assert progress.solve_seconds("p") == 90


def test_a_solve_with_no_timing_has_no_solve_seconds(progress_file):
    progress.record("p", True, today=D(2026, 1, 1))
    assert progress.solve_seconds("p") is None


def test_reset_all_forgets_the_time_spent(progress_file, tmp_path):
    progress.add_seconds("p", 30)
    progress.reset_all(backup_dir=tmp_path / "backups")
    assert progress.seconds("p") == 0
