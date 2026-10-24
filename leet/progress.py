import contextlib
import json
import threading

try:
    import fcntl
except ImportError:  # Windows: threads in one process are still safe, separate processes are not
    fcntl = None

from leet.fsutil import atomic_write_text
from leet.problems import ROOT

PATH = ROOT / "progress.json"
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


def set_current(key):
    with _locked():
        data = load()
        data["current"] = key
        save(data)


def record(key, solved):
    with _locked():
        data = load()
        entry = data["problems"].setdefault(key, {"attempts": 0, "solved": False})
        entry["attempts"] += 1
        entry["solved"] = entry["solved"] or solved
        save(data)


def status(key):
    entry = load()["problems"].get(key)
    if not entry:
        return "todo"
    return "solved" if entry["solved"] else "attempted"
