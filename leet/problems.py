import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
REFERENCE_DIR = ROOT / "reference"


@dataclass(frozen=True)
class Problem:
    dir: Path
    id: int
    title: str
    category: str
    difficulty: str
    method: str
    compare: str = "exact"
    timeout: float = 5.0
    arg_types: tuple = None
    return_type: str = "plain"
    inplace: int = None
    design: str = None
    roundtrip: dict = None
    checker: bool = False
    complexity: dict = None
    hidden: bool = False

    @property
    def key(self):
        return self.dir.name

    @property
    def solution_path(self):
        return self.dir / "solution.py"

    @property
    def readme_path(self):
        return self.dir / "README.md"

    @property
    def starter_path(self):
        return self.dir / "starter.py"

    def load_starter(self):
        return self.starter_path.read_text()

    @property
    def hints_path(self):
        return self.dir / "hints.json"

    def load_hints(self):
        return json.loads(self.hints_path.read_text()) if self.hints_path.exists() else []

    @property
    def checker_path(self):
        return self.dir / "check.py"

    @property
    def explanation_path(self):
        return self.dir / "explanation.md"

    def load_explanation(self):
        return self.explanation_path.read_text() if self.explanation_path.exists() else None

    @property
    def hidden_path(self):
        return self.dir / "hidden.py"

    @property
    def reference_path(self):
        return REFERENCE_DIR / f"{self.key}.py"

    def load_cases(self):
        return json.loads((self.dir / "tests.json").read_text())

    def param_names(self):
        """Names for the arguments of a case, as the starter code spells them, for labelling inputs."""
        if self.design:
            return ["operations", "arguments"]
        method = self.roundtrip["encode"] if self.roundtrip else self.method
        found = re.search(rf"def {re.escape(method)}\(self,?(.*?)\)\s*(?:->|:)", self.load_starter(), re.DOTALL)
        names, depth, current = [], 0, ""
        for ch in (found.group(1) if found else "") + ",":
            if ch == "," and depth == 0:
                if current.strip():
                    names.append(re.split(r"[:=]", current, 1)[0].strip())
                current = ""
                continue
            depth += ch in "(["
            depth -= ch in "])"
            current += ch
        return names

    @property
    def notes_path(self):
        return self.dir / "notes.md"

    def load_notes(self):
        return self.notes_path.read_text() if self.notes_path.exists() else ""

    @property
    def custom_path(self):
        return self.dir / "custom.json"

    def load_custom(self):
        return json.loads(self.custom_path.read_text()) if self.custom_path.exists() else []


def _load(meta_path):
    meta = json.loads(meta_path.read_text())
    if meta.get("arg_types") is not None:
        meta["arg_types"] = tuple(meta["arg_types"])
    return Problem(dir=meta_path.parent, **meta)


def all_problems():
    metas = sorted(PROBLEMS_DIR.glob("*/*/meta.json"))
    return sorted((_load(m) for m in metas), key=lambda p: p.id)


def find(query):
    """Resolve an id (3, 003), folder name, slug, or a path inside a problem folder."""
    problems = all_problems()
    path = Path(query)
    if path.exists():
        resolved = path.resolve()
        for p in problems:
            if p.dir == resolved or p.dir in resolved.parents:
                return p
    for p in problems:
        if query == p.key or query == p.key.split("-", 1)[1]:
            return p
    if query.isdigit():
        for p in problems:
            if p.id == int(query):
                return p
    raise LookupError(f"no problem matches {query!r}")
