import json
import mimetypes
import re
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from leet import progress
from leet.fsutil import atomic_write_text
from leet.execute import all_passed, run_perf, run_problem
from leet.problems import all_problems, find
from leet.reset import reset

WEB_DIR = Path(__file__).resolve().parent / "web"
MAX_BODY = 1_000_000
HINTS_BLOCK = re.compile(r"\n<details>.*?</details>\n", re.DOTALL)


def _problem_summary(p, tried=None):
    status, due = (tried if tried is not None else progress.summary()).get(p.key, ("todo", False))
    return {
        "key": p.key,
        "id": p.id,
        "title": p.title,
        "category": p.category,
        "difficulty": p.difficulty,
        "status": status,
        "due": due,
    }


def make_handler():
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass

        def _send(self, status, body, content_type):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, payload, status=200):
            self._send(status, json.dumps(payload).encode(), "application/json")

        def _error(self, status, message):
            self._json({"error": message}, status)

        def _trusted(self):
            """Reject requests from other sites or via DNS rebinding.

            The API writes and runs code, so only the page we serve may call it.
            """
            port = self.server.server_address[1]
            allowed_hosts = {f"localhost:{port}", f"127.0.0.1:{port}"}
            if self.headers.get("Host") not in allowed_hosts:
                return False
            origin = self.headers.get("Origin")
            if origin and urlparse(origin).netloc not in allowed_hosts:
                return False
            return True

        def _body(self):
            length = int(self.headers.get("Content-Length") or 0)
            if length > MAX_BODY:
                raise ValueError("request too large")
            return json.loads(self.rfile.read(length) or b"{}")

        def do_GET(self):
            if not self._trusted():
                return self._error(403, "forbidden")
            path = urlparse(self.path).path
            if path == "/api/problems":
                tried = progress.summary()
                return self._json([_problem_summary(p, tried) for p in all_problems()])
            if path.startswith("/api/problems/"):
                parts = path.removeprefix("/api/problems/").split("/")
                if len(parts) == 3 and parts[1] == "hint":
                    return self._get_hint(parts[0], parts[2])
                if len(parts) == 2 and parts[1] == "solution":
                    force = parse_qs(urlparse(self.path).query).get("force") == ["1"]
                    return self._get_solution(parts[0], force)
                return self._get_problem(parts[0])
            self._static(path)

        def _get_problem(self, key):
            try:
                p = find(key)
            except LookupError:
                return self._error(404, "no such problem")
            self._json({
                **_problem_summary(p),
                "readme": HINTS_BLOCK.sub("\n", p.readme_path.read_text()),
                "code": p.solution_path.read_text(),
                "hint_count": len(p.load_hints()),
                "complexity": p.complexity,
            })

        def _get_solution(self, key, force):
            try:
                p = find(key)
            except LookupError:
                return self._error(404, "no such problem")
            solved = progress.status(p.key) == "solved"
            if not solved and not force:
                return self._json({"error": "Solve this problem first, or ask for it explicitly.", "solved": False}, 403)
            self._json({
                "reference": p.reference_path.read_text(),
                "complexity": p.complexity,
                "solved": solved,
            })

        def _get_hint(self, key, n):
            try:
                hints = find(key).load_hints()
            except LookupError:
                return self._error(404, "no such problem")
            if not n.isdigit() or not 1 <= int(n) <= len(hints):
                return self._error(404, "no such hint")
            self._json({"hint": hints[int(n) - 1]})

        def _static(self, path):
            rel = "index.html" if path == "/" else path.lstrip("/")
            target = (WEB_DIR / rel).resolve()
            if WEB_DIR not in target.parents or not target.is_file():
                return self._error(404, "not found")
            ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
            self._send(200, target.read_bytes(), ctype)

        def do_POST(self):
            if not self._trusted():
                return self._error(403, "forbidden")
            if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                return self._error(415, "expected application/json")
            parts = urlparse(self.path).path.strip("/").split("/")
            if len(parts) != 4 or parts[:2] != ["api", "problems"]:
                return self._error(404, "not found")
            try:
                p = find(parts[2])
                body = self._body()
            except LookupError:
                return self._error(404, "no such problem")
            except (ValueError, json.JSONDecodeError) as exc:
                return self._error(400, str(exc))
            if parts[3] == "reset":
                backup = reset(p)
                return self._json({"code": p.load_starter(), "backed_up": backup is not None})
            code = body.get("code")
            if not isinstance(code, str):
                return self._error(400, "missing code")
            if parts[3] == "save":
                atomic_write_text(p.solution_path, code)
                return self._json({"ok": True})
            if parts[3] == "run":
                atomic_write_text(p.solution_path, code)
                outcome = run_problem(p)
                progress.set_current(p.key)
                progress.record(p.key, all_passed(outcome))
                outcome["status"], outcome["due"] = progress.summary().get(p.key, ("todo", False))
                return self._json(outcome)
            if parts[3] == "perf":
                atomic_write_text(p.solution_path, code)
                return self._json(run_perf(p))
            self._error(404, "not found")

    return Handler


def make_server(port):
    return ThreadingHTTPServer(("127.0.0.1", port), make_handler())


def serve(port=8765, open_browser=True):
    try:
        server = make_server(port)
    except OSError as exc:
        raise SystemExit(f"cannot listen on port {port}: {exc}")
    url = f"http://localhost:{port}/"
    print(f"offline-leet running at {url}  (Ctrl+C to stop)")
    if open_browser:
        threading.Timer(0.5, webbrowser.open, args=[url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
