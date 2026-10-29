import contextlib
import datetime
import json
import threading
import time

try:
    import fcntl
except ImportError:  # Windows: threads in one process are still safe, separate processes are not
    fcntl = None

from leet.fsutil import atomic_write_text
from leet.problems import ROOT
from leet.reset import BACKUP_DIR

PATH = ROOT / "progress.json"
REVIEW_DAYS = (1, 3, 7, 14, 30)  # days until a solved problem is due, by box 1 to 5
_lock = threading.RLock()
_depth = 0
_handle = None


@contextlib.contextmanager
def _locked():
    """Exclusive access across threads and, where flock exists, across processes."""
    global _depth, _handle
    with _lock:
        if _depth == 0 and fcntl:
            _handle = open(PATH.with_name(PATH.name + ".lock"), "a")
            fcntl.flock(_handle, fcntl.LOCK_EX)
        _depth += 1
        try:
            yield
        finally:
            _depth -= 1
            if _depth == 0 and _handle:
                fcntl.flock(_handle, fcntl.LOCK_UN)
                _handle.close()
                _handle = None


def _empty():
    return {"current": None, "problems": {}}


def load():
    with _locked():
        if not PATH.exists():
            return _empty()
        try:
            return json.loads(PATH.read_text())
        except json.JSONDecodeError:
            # Keep the unreadable file so the next save does not silently destroy it.
            PATH.replace(PATH.with_name(PATH.name + ".corrupt"))
            return _empty()


def save(data):
    with _locked():
        atomic_write_text(PATH, json.dumps(data, indent=2))


def reset_all(backup_dir=None):
    """Forget all progress, keeping the old file in the backup folder.

    Returns the backup path, or None if there was no progress file. Solutions are untouched.
    """
    backup_dir = BACKUP_DIR if backup_dir is None else backup_dir
    with _locked():
        backup = None
        if PATH.exists():
            backup_dir.mkdir(parents=True, exist_ok=True)
            stamp = time.strftime("%Y%m%d-%H%M%S")
            backup = backup_dir / f"progress-{stamp}.json"
            n = 1
            while backup.exists():
                backup = backup_dir / f"progress-{stamp}-{n}.json"
                n += 1
            atomic_write_text(backup, PATH.read_text())
        save(_empty())
        return backup


def set_current(key):
    with _locked():
        data = load()
        data["current"] = key
        save(data)


def record(key, solved, today=None):
    """Count a run. Passing a due review moves the problem up a box; failing one resets it."""
    today = today or datetime.date.today()
    with _locked():
        data = load()
        entry = data["problems"].setdefault(key, {"attempts": 0, "solved": False})
        was_due = _is_due(entry, today)
        entry["attempts"] += 1
        entry["last_attempt"] = today.isoformat()
        if solved:
            first_time = not entry["solved"]
            entry["solved"] = True
            entry.setdefault("solved_at", today.isoformat())
            if first_time:
                _schedule(entry, 1, today)
            elif was_due:
                _schedule(entry, entry.get("box", 1) + 1, today)
        elif was_due:
            _schedule(entry, 1, today)
        save(data)


def _schedule(entry, box, today):
    entry["box"] = min(box, len(REVIEW_DAYS))
    due = today + datetime.timedelta(days=REVIEW_DAYS[entry["box"] - 1])
    entry["due"] = due.isoformat()


def _is_due(entry, today):
    """Solved problems come back for review. Ones solved before this tracking are due now."""
    if not entry.get("solved"):
        return False
    return datetime.date.fromisoformat(entry.get("due", today.isoformat())) <= today


def due_reviews(today=None):
    """Keys of solved problems due for review, the longest overdue first."""
    today = today or datetime.date.today()
    problems = load()["problems"]
    due = [(e.get("due", "0000-00-00"), k) for k, e in problems.items() if _is_due(e, today)]
    return [key for _, key in sorted(due)]


def status(key):
    entry = load()["problems"].get(key)
    if not entry:
        return "todo"
    return "solved" if entry["solved"] else "attempted"


def due_on(key):
    """ISO date a solved problem next comes up for review, or None if it is not solved."""
    entry = load()["problems"].get(key)
    return entry.get("due") if entry and entry["solved"] else None


def summary(today=None):
    """{key: (status, due)} for every problem that has been tried, from one read of the file."""
    today = today or datetime.date.today()
    out = {}
    for key, entry in load()["problems"].items():
        status = "solved" if entry["solved"] else "attempted"
        out[key] = (status, _is_due(entry, today))
    return out
