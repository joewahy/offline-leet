"""Hidden tests: big inputs that are generated on demand instead of stored in git.

A problem with "hidden": true in meta.json has a hidden.py next to it defining
generate(rng), which returns a list of argument lists. Expected values come
from the reference solution. The finished cases are cached in .leet-cache/ and
rebuilt whenever hidden.py or the reference changes.
"""
import hashlib
import importlib.util
import json
import random

from leet.problems import ROOT

CACHE_DIR = ROOT / ".leet-cache" / "hidden"
SUMMARY_CHARS = 200


def fingerprint(problem):
    digest = hashlib.sha256()
    for path in (problem.hidden_path, problem.reference_path):
        digest.update(path.read_bytes())
    return digest.hexdigest()


def cache_path(problem):
    return CACHE_DIR / f"{problem.key}.json"


def load_cached(problem):
    try:
        data = json.loads(cache_path(problem).read_text())
    except (OSError, json.JSONDecodeError):
        return None
    return data["cases"] if data.get("fingerprint") == fingerprint(problem) else None


def store(problem, cases):
    from leet.fsutil import atomic_write_text

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {"fingerprint": fingerprint(problem), "cases": cases}
    atomic_write_text(cache_path(problem), json.dumps(payload))


def generate_args(problem):
    """Run hidden.py's generate(rng). The seed is the problem id, so it is repeatable."""
    spec = importlib.util.spec_from_file_location("hidden", problem.hidden_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.generate(random.Random(problem.id))


def shorten(value):
    text = repr(value)
    return text if len(text) <= SUMMARY_CHARS else text[: SUMMARY_CHARS - 3] + "..."
