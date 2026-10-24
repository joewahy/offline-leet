"""Restore a problem's solution.py to its starter code, keeping a backup of what was there."""
import time

from leet.fsutil import atomic_write_text
from leet.problems import ROOT

BACKUP_DIR = ROOT / ".leet-backups"


def reset(problem, backup_dir=None):
    """Replace solution.py with the starter code.

    Returns the path of the backup holding your previous code, or None if there
    was nothing to back up (the file was missing or already the starter).
    """
    backup_dir = BACKUP_DIR if backup_dir is None else backup_dir
    starter = problem.load_starter()
    path = problem.solution_path
    current = path.read_text() if path.exists() else None
    backup = None
    if current is not None and current != starter:
        folder = backup_dir / problem.key
        folder.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        backup = folder / f"{stamp}.py"
        n = 1
        while backup.exists():
            backup = folder / f"{stamp}-{n}.py"
            n += 1
        atomic_write_text(backup, current)
    atomic_write_text(path, starter)
    return backup
