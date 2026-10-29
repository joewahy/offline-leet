"""The local web server's API, against a real server on a free port."""
import json
import threading
import urllib.error
import urllib.request

import pytest

from leet import progress, reset as reset_module
from leet.problems import find
from leet.server import make_server

PROBLEM = "009-longest-consecutive-sequence"


@pytest.fixture
def server():
    srv = make_server(0)
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()
    srv.server_close()


@pytest.fixture
def untouched_solution():
    """The API writes solution.py when running code; put it back afterwards."""
    path = find(PROBLEM).solution_path
    original = path.read_bytes()
    yield path
    path.write_bytes(original)


def call(base, path, body=None, headers=None):
    request = urllib.request.Request(
        base + path,
        data=None if body is None else json.dumps(body).encode(),
        headers={"Content-Type": "application/json", **(headers or {})},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as exc:
        return exc.code, json.load(exc)


def test_problem_payload_has_hints_and_target_complexity(server):
    status, data = call(server, f"/api/problems/{PROBLEM}")
    assert status == 200
    assert data["hint_count"] == 3
    assert "<details>" not in data["readme"]
    assert data["complexity"]["time"] == "O(n)"


def test_hints_are_served_one_at_a_time(server):
    assert call(server, f"/api/problems/{PROBLEM}/hint/1")[0] == 200
    assert call(server, f"/api/problems/{PROBLEM}/hint/4")[0] == 404
    assert call(server, f"/api/problems/{PROBLEM}/hint/0")[0] == 404


def test_foreign_host_is_rejected(server):
    assert call(server, "/api/problems", headers={"Host": "evil.example"})[0] == 403


def test_perf_endpoint_rejects_a_failing_solution(server, untouched_solution):
    starter = untouched_solution.read_text()
    status, report = call(server, f"/api/problems/{PROBLEM}/perf", {"code": starter})
    assert status == 200
    assert "does not pass all the tests" in report["error"]


def test_perf_endpoint_measures_a_passing_solution(server, untouched_solution):
    reference = find(PROBLEM).reference_path.read_text()
    status, report = call(server, f"/api/problems/{PROBLEM}/perf", {"code": reference})
    assert status == 200
    assert report["time"]["verdict"] in ("faster", "similar")
    assert report["target"]["space"] == "O(n)"


@pytest.fixture
def sandboxed_state(tmp_path, monkeypatch):
    """Keep progress and backups out of the real project files."""
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    monkeypatch.setattr(reset_module, "BACKUP_DIR", tmp_path / "backups")
    return tmp_path


def test_reset_endpoint_restores_the_starter_and_backs_up(server, untouched_solution, sandboxed_state):
    problem = find(PROBLEM)
    call(server, f"/api/problems/{PROBLEM}/save", {"code": "my edit\n"})
    status, data = call(server, f"/api/problems/{PROBLEM}/reset", {})
    assert status == 200
    assert data["code"] == problem.load_starter()
    assert data["backed_up"] is True
    assert untouched_solution.read_text() == problem.load_starter()
    backups = list((sandboxed_state / "backups" / PROBLEM).glob("*.py"))
    assert [b.read_text() for b in backups] == ["my edit\n"]


def test_reference_solution_is_locked_until_solved(server, sandboxed_state):
    status, data = call(server, f"/api/problems/{PROBLEM}/solution")
    assert status == 403
    assert "reference" not in data


def test_reference_solution_can_be_requested_explicitly(server, sandboxed_state):
    status, data = call(server, f"/api/problems/{PROBLEM}/solution?force=1")
    assert status == 200
    assert data["reference"] == find(PROBLEM).reference_path.read_text()
    assert data["solved"] is False
    assert data["complexity"]["time"] == "O(n)"


def test_reference_solution_opens_once_solved(server, sandboxed_state):
    progress.record(PROBLEM, True)
    status, data = call(server, f"/api/problems/{PROBLEM}/solution")
    assert status == 200
    assert data["solved"] is True


def test_problem_list_marks_solved_problems_that_are_due_for_review(server, tmp_path, monkeypatch):
    import datetime

    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    progress.record("001-contains-duplicate", True, today=datetime.date(2020, 1, 1))
    progress.record(PROBLEM, True)
    _, rows = call(server, "/api/problems")
    by_key = {r["key"]: r for r in rows}
    assert (by_key["001-contains-duplicate"]["status"], by_key["001-contains-duplicate"]["due"]) == ("solved", True)
    assert (by_key[PROBLEM]["status"], by_key[PROBLEM]["due"]) == ("solved", False)
    assert by_key["002-valid-anagram"]["due"] is False


def test_solution_response_includes_the_explanation_when_there_is_one(server):
    status, data = call(server, "/api/problems/001-contains-duplicate/solution?force=1")
    assert status == 200
    assert data["explanation"].startswith("### Approach")
    status, data = call(server, "/api/problems/002-valid-anagram/solution?force=1")
    assert "explanation" in data


def test_progress_reset_clears_progress(server, tmp_path, monkeypatch):
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    monkeypatch.setattr(progress, "BACKUP_DIR", tmp_path / "backups")
    progress.record(PROBLEM, True)
    status, data = call(server, "/api/progress/reset", {})
    assert (status, data) == (200, {"backed_up": True})
    assert progress.summary() == {}


def test_time_endpoint_adds_to_the_problem_total(server, tmp_path, monkeypatch):
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    assert call(server, f"/api/problems/{PROBLEM}/time", {"seconds": 20})[1] == {"seconds": 20}
    assert call(server, f"/api/problems/{PROBLEM}/time", {"seconds": 5})[1] == {"seconds": 25}
    status, data = call(server, f"/api/problems/{PROBLEM}")
    assert (data["seconds"], data["solve_seconds"]) == (25, None)
    assert progress.summary() == {}


@pytest.mark.parametrize("seconds", [0, -5, 3601, "9", True, None, float("nan")])
def test_time_endpoint_rejects_bad_values(server, tmp_path, monkeypatch, seconds):
    monkeypatch.setattr(progress, "PATH", tmp_path / "progress.json")
    status, data = call(server, f"/api/problems/{PROBLEM}/time", {"seconds": seconds})
    assert status == 400
    assert progress.seconds(PROBLEM) == 0
