"""Atomic file writes and the progress file's resilience to concurrency and corruption."""
import json
import os
import threading

import pytest

from leet import progress
from leet.fsutil import atomic_write_text


@pytest.fixture
def progress_file(tmp_path, monkeypatch):
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    return progress.PATH


def test_write_creates_and_replaces(tmp_path):
    path = tmp_path / "a.py"
    atomic_write_text(path, "one")
    atomic_write_text(path, "two")
    assert path.read_text() == "two"
    assert [p.name for p in tmp_path.iterdir()] == ["a.py"]


def test_failed_write_keeps_old_content_and_leaves_no_temp(tmp_path, monkeypatch):
    path = tmp_path / "a.py"
    path.write_text("precious")

    def boom(src, dst):
        raise OSError("disk full")

    monkeypatch.setattr(os, "replace", boom)
    with pytest.raises(OSError):
        atomic_write_text(path, "new")
    assert path.read_text() == "precious"
    assert [p.name for p in tmp_path.iterdir()] == ["a.py"]


def test_existing_file_mode_is_preserved(tmp_path):
    path = tmp_path / "a.py"
    path.write_text("x")
    path.chmod(0o640)
    atomic_write_text(path, "y")
    assert path.stat().st_mode & 0o777 == 0o640


def test_concurrent_records_are_not_lost(progress_file):
    threads = [threading.Thread(target=progress.record, args=("p", False)) for _ in range(40)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert progress.load()["problems"]["p"]["attempts"] == 40


def test_corrupt_progress_is_set_aside_not_overwritten(progress_file):
    progress_file.write_text("{ not json")
    assert progress.status("p") == "todo"
    progress.record("p", True)
    assert progress.status("p") == "solved"
    assert progress_file.with_name("progress.json.corrupt").read_text() == "{ not json"
    json.loads(progress_file.read_text())


def test_concurrent_processes_do_not_lose_records(progress_file):
    import subprocess
    import sys
    import textwrap

    code = textwrap.dedent(f"""
        from pathlib import Path
        from leet import progress
        progress.PATH = Path({str(progress_file)!r})
        for _ in range(30):
            progress.record("p", False)
    """)
    procs = [subprocess.Popen([sys.executable, "-c", code]) for _ in range(5)]
    assert all(p.wait(timeout=60) == 0 for p in procs)
    assert progress.load()["problems"]["p"]["attempts"] == 150
