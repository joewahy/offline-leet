import json
import threading

from leet.fsutil import atomic_write_text
from leet.problems import ROOT

PATH = ROOT / "progress.json"
_lock = threading.RLock()


def _empty():
    return {"current": None, "problems": {}}


def load():
    with _lock:
        if not PATH.exists():
            return _empty()
        try:
            return json.loads(PATH.read_text())
        except json.JSONDecodeError:
            # Keep the unreadable file so the next save does not silently destroy it.
            PATH.replace(PATH.with_name(PATH.name + ".corrupt"))
            return _empty()


def save(data):
    with _lock:
        atomic_write_text(PATH, json.dumps(data, indent=2))


def set_current(key):
    with _lock:
        data = load()
        data["current"] = key
        save(data)


def record(key, solved):
    with _lock:
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
