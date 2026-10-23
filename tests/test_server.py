"""The local web server's API, against a real server on a free port."""
import json
import threading
import urllib.error
import urllib.request

import pytest

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
