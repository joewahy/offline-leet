import json

from leet.problems import ROOT

PATH = ROOT / "progress.json"


def load():
    if PATH.exists():
        return json.loads(PATH.read_text())
    return {"current": None, "problems": {}}


def save(data):
    PATH.write_text(json.dumps(data, indent=2))


def set_current(key):
    data = load()
    data["current"] = key
    save(data)


def record(key, solved):
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
