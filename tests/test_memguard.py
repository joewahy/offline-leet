"""The memory watchdog, exercised in child processes so the limit only hits them."""
import subprocess
import sys
import textwrap

CHUNK = 20 * 1024 * 1024


def run(code):
    return subprocess.run(
        [sys.executable, "-c", textwrap.dedent(code)], capture_output=True, text=True, timeout=60
    )


def test_hog_is_interrupted_inside_the_guard():
    proc = run(f"""
        import time
        from leet import memguard
        memguard.start(limit=300 * 1024 * 1024)
        hog = []
        try:
            with memguard.guard():
                while True:
                    hog.append(bytearray(b"x") * {CHUNK})
                    time.sleep(0.001)
        except memguard.MemoryLimitExceeded as exc:
            print(exc)
    """)
    assert proc.stdout.strip() == "memory limit exceeded (300 MB)", proc.stderr


def test_code_that_swallows_the_error_is_still_stopped():
    proc = run(f"""
        import time
        from leet import memguard
        memguard.start(limit=200 * 1024 * 1024)
        hog = []
        with memguard.guard():
            while True:
                try:
                    hog.append(bytearray(b"x") * {CHUNK})
                    time.sleep(0.001)
                except BaseException:
                    pass
    """)
    assert proc.returncode == 137
    assert "memory limit exceeded (200 MB)" in proc.stderr


def test_runner_reports_the_memory_error_on_the_case():
    proc = run(f"""
        import dataclasses, time, types
        from leet import memguard, runner
        from leet.problems import find
        memguard.start(limit=300 * 1024 * 1024)
        problem = find("009")
        class Solution:
            def longestConsecutive(self, *args):
                hog = []
                while True:
                    hog.append(bytearray(b"x") * {CHUNK})
                    time.sleep(0.001)
        module = types.SimpleNamespace(Solution=Solution)
        case = problem.load_cases()[0]
        result = runner.run_case(problem, module, None, case)
        print(result["ok"], result["error"])
    """)
    assert proc.stdout.strip() == "False memory limit exceeded (300 MB)", proc.stderr
