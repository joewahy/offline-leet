import json
import subprocess
import sys


def run_problem(problem, reference=False):
    """Run a problem's cases in a subprocess. Returns the runner's JSON as a dict."""
    cmd = [sys.executable, "-m", "leet.runner", problem.key]
    if reference:
        cmd.append("--reference")
    budget = problem.timeout * len(problem.load_cases()) + 5
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=budget)
    except subprocess.TimeoutExpired:
        return {"load_error": f"timed out after {budget:.0f}s"}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"load_error": proc.stderr.strip() or "runner produced no output"}
