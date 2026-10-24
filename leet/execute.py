import json
import subprocess
import sys

HIDDEN_BUDGET = 180  # seconds for generating and running the hidden cases


def run_problem(problem, reference=False):
    """Run a problem's cases in a subprocess. Returns the runner's JSON as a dict."""
    cmd = [sys.executable, "-m", "leet.runner", problem.key]
    if reference:
        cmd.append("--reference")
    budget = problem.timeout * len(problem.load_cases()) + 5
    if problem.hidden:
        budget += HIDDEN_BUDGET
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=budget)
    except subprocess.TimeoutExpired:
        return {"load_error": f"timed out after {budget:.0f}s"}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"load_error": proc.stderr.strip() or "runner produced no output"}


def run_perf(problem, solution_path=None):
    """Compare a solution's speed and memory with the reference, in a subprocess."""
    cmd = [sys.executable, "-m", "leet.perf", problem.key]
    if solution_path:
        cmd.append(str(solution_path))
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return {"error": "The performance check took too long and was stopped."}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"error": proc.stderr.strip() or "The performance check produced no output."}


def all_passed(outcome):
    """True when every visible case passed and, if there are hidden tests, those did too."""
    results = outcome.get("results")
    if not results or not all(r["ok"] for r in results):
        return False
    hidden = outcome.get("hidden")
    return hidden is None or not ({"error", "failure"} & hidden.keys())
