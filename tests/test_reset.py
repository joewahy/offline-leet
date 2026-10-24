"""Restoring starter code, with a backup of what was replaced."""
import dataclasses
import shutil

import pytest

from leet.problems import find
from leet.reset import reset


@pytest.fixture
def problem(tmp_path):
    """A throwaway copy of a real problem, so the real solution.py is never touched."""
    real = find("009")
    folder = tmp_path / "problem"
    folder.mkdir()
    shutil.copy(real.starter_path, folder / "starter.py")
    shutil.copy(real.starter_path, folder / "solution.py")
    return dataclasses.replace(real, dir=folder)


def test_edited_solution_is_backed_up_and_restored(problem, tmp_path):
    problem.solution_path.write_text("my work in progress\n")
    backup = reset(problem, backup_dir=tmp_path / "backups")
    assert backup.read_text() == "my work in progress\n"
    assert backup.parent.name == problem.key
    assert problem.solution_path.read_text() == problem.load_starter()


def test_untouched_solution_needs_no_backup(problem, tmp_path):
    assert reset(problem, backup_dir=tmp_path / "backups") is None
    assert not (tmp_path / "backups").exists()
    assert problem.solution_path.read_text() == problem.load_starter()


def test_missing_solution_file_is_recreated(problem, tmp_path):
    problem.solution_path.unlink()
    assert reset(problem, backup_dir=tmp_path / "backups") is None
    assert problem.solution_path.read_text() == problem.load_starter()


def test_two_resets_in_the_same_second_keep_both_backups(problem, tmp_path):
    backups = tmp_path / "backups"
    problem.solution_path.write_text("first\n")
    one = reset(problem, backup_dir=backups)
    problem.solution_path.write_text("second\n")
    two = reset(problem, backup_dir=backups)
    assert one != two
    assert (one.read_text(), two.read_text()) == ("first\n", "second\n")
