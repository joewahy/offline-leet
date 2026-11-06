"""Pull your NeetCode submissions from a public GitHub repo into the problems' solution.py files.

Only problems whose solution.py is still the starter are filled in, so code you wrote here is never
overwritten. An imported solution counts as solved only if it passes this app's own tests.
"""
import json
import os
import re
import shutil
import subprocess
import threading
import time
from pathlib import Path

from leet import progress
from leet.execute import all_passed, run_problem
from leet.fsutil import atomic_write_text
from leet.problems import ROOT, all_problems

SETTINGS_PATH = ROOT / ".leet-sync.json"
CACHE_DIR = ROOT / ".leet-cache" / "neetcode"
ALIASES_PATH = Path(__file__).with_name("neetcode_aliases.json")
REPO_URL = re.compile(r"^https://github\.com/[\w.-]+/[\w.-]+?(\.git)?/?$")
SUBMISSION = re.compile(r"^submission-(\d+)\.(\w+)$")
GIT_TIMEOUT = 120


def load_repo():
    try:
        return json.loads(SETTINGS_PATH.read_text()).get("repo", "")
    except (OSError, json.JSONDecodeError):
        return ""


def save_repo(url):
    if not REPO_URL.match(url):
        raise ValueError("Enter a public GitHub repository URL, like https://github.com/you/neetcode-submissions-abc")
    atomic_write_text(SETTINGS_PATH, json.dumps({"repo": url}, indent=2))


def _git(*args, cwd=None):
    # Only https is allowed, and the URL is never read as an option, so a hostile URL cannot run anything.
    env = {**os.environ, "GIT_ALLOW_PROTOCOL": "https", "GIT_TERMINAL_PROMPT": "0"}
    proc = subprocess.run(["git", *args], cwd=cwd, env=env, capture_output=True, text=True, timeout=GIT_TIMEOUT)
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else "git failed")
    return proc.stdout.strip()


def fetch(url):
    """Make CACHE_DIR a fresh shallow copy of the repo's default branch."""
    if (CACHE_DIR / ".git").is_dir():
        try:
            if _git("config", "remote.origin.url", cwd=CACHE_DIR) == url:
                _git("fetch", "--depth", "1", "origin", "HEAD", cwd=CACHE_DIR)
                _git("reset", "--hard", "FETCH_HEAD", cwd=CACHE_DIR)
                return
        except (RuntimeError, subprocess.TimeoutExpired):
            pass
    shutil.rmtree(CACHE_DIR, ignore_errors=True)
    CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)
    _git("clone", "--depth", "1", "--", url, str(CACHE_DIR))


def scan(root):
    """{slug: {extension: (number, path)}} holding the newest submission per problem and language."""
    found = {}
    for path in root.rglob("submission-*.*"):
        match = SUBMISSION.match(path.name)
        if not match or ".git" in path.relative_to(root).parts:
            continue
        number, ext = int(match.group(1)), match.group(2)
        best = found.setdefault(path.parent.name, {})
        if ext not in best or number > best[ext][0]:
            best[ext] = (number, path)
    return found


# NeetCode runs submissions with these already imported; this app expects each file to import what it uses.
MODULES = ("heapq", "collections", "math", "bisect", "itertools", "functools", "string", "random")
NAMES = {
    "deque": "collections", "defaultdict": "collections", "Counter": "collections", "OrderedDict": "collections",
    "heappush": "heapq", "heappop": "heapq", "heapify": "heapq", "heappushpop": "heapq", "heapreplace": "heapq",
    "bisect_left": "bisect", "bisect_right": "bisect", "cache": "functools", "lru_cache": "functools",
    "inf": "math",
}


def add_imports(code):
    """Prepend the imports NeetCode would have supplied for the modules and names the code uses."""
    def has(name):
        return re.search(rf"^\s*(import|from)\s+.*\b{name}\b|^\s*{name}\s*=|^\s*(def|class)\s+{name}\b", code, re.M)

    lines = [f"import {m}" for m in MODULES if re.search(rf"\b{m}\.\w", code) and not has(m)]
    for name, module in NAMES.items():
        if re.search(rf"(?<![\w.]){name}\b", code) and not has(name):
            lines.append(f"from {module} import {name}")
    return "\n".join(lines) + "\n\n" + code if lines else code


def rename_entry(code, method):
    """NeetCode sometimes names the entry method differently. Rename it when there is one clear candidate."""
    defs = re.findall(r"^[ \t]+def (\w+)\(self", code, re.M)
    if method in defs:
        return code
    entries = [d for d in defs if not d.startswith("_") and not re.search(rf"self\.{d}\b", code)]
    if len(entries) != 1:
        return code
    return re.sub(rf"^([ \t]+def ){entries[0]}\(self", rf"\g<1>{method}(self", code, count=1, flags=re.M)


def _same(a, b):
    return a.strip() == b.strip()


def _resolve(slug, by_key):
    key = json.loads(ALIASES_PATH.read_text()).get(slug)
    if key in by_key:
        return by_key[key]
    return next((p for k, p in by_key.items() if k.split("-", 1)[1] == slug), None)


def _import_one(slug, langs, by_key):
    """Return a result dict for one NeetCode folder, importing its code when allowed."""
    result = {"slug": slug}
    if "py" not in langs:
        return {**result, "status": "skipped", "detail": "Only " + ", ".join(sorted(langs)) + " submissions"}
    problem = _resolve(slug, by_key)
    if problem is None:
        return {**result, "status": "unmatched", "detail": "No matching problem here"}
    result.update(key=problem.key, title=problem.title)
    code = langs["py"][1].read_text()
    if not problem.design:
        code = rename_entry(code, problem.method)
    code = add_imports(code)
    current = problem.solution_path.read_text() if problem.solution_path.exists() else ""
    if _same(current, code):
        return {**result, "status": "current", "detail": "Already has this code"}
    if not _same(current, problem.load_starter()) or progress.status(problem.key) == "solved":
        return {**result, "status": "kept", "detail": "You already have your own code"}
    atomic_write_text(problem.solution_path, code if code.endswith("\n") else code + "\n")
    outcome = run_problem(problem)
    if all_passed(outcome):
        progress.record(problem.key, True)
        return {**result, "status": "solved", "detail": "Passes the tests"}
    detail = outcome.get("load_error") or "Does not pass the tests here yet"
    return {**result, "status": "imported", "detail": detail}


_lock = threading.Lock()
_state = {"running": False, "done": 0, "total": 0, "results": [], "error": None, "finished_at": None}


def state():
    with _lock:
        return {**_state, "results": list(_state["results"]), "repo": load_repo()}


def start(url):
    """Begin a sync in the background. Returns False if one is already running."""
    with _lock:
        if _state["running"]:
            return False
        _state.update(running=True, done=0, total=0, results=[], error=None, finished_at=None)
    threading.Thread(target=_run, args=(url,), daemon=True).start()
    return True


def _run(url):
    try:
        fetch(url)
        found = scan(CACHE_DIR)
        by_key = {p.key: p for p in all_problems()}
        with _lock:
            _state["total"] = len(found)
        for slug in sorted(found):
            result = _import_one(slug, found[slug], by_key)
            with _lock:
                _state["results"].append(result)
                _state["done"] += 1
    except subprocess.TimeoutExpired:
        _fail("Timed out talking to GitHub")
    except Exception as exc:  # shown to the user rather than lost in a thread
        _fail(str(exc))
    finally:
        with _lock:
            _state["running"] = False
            _state["finished_at"] = time.strftime("%Y-%m-%d %H:%M")


def _fail(message):
    with _lock:
        _state["error"] = message
