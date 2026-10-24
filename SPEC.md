# offline-leet: spec

Practice the NeetCode 150 offline, in Python, from VS Code.

## Decisions

- Language: Python only.
- Problem set: NeetCode 150 (names and categories only; statements, tests, and reference solutions are written by us, not copied from LeetCode).
- Workflow: VS Code. No web UI.
- Offline: no network needed after initial setup. No CDNs, no runtime downloads.

## Runtime: Dev Container (recommended) vs plain venv

Python-only + VS Code makes a custom web app and a custom sandbox service unnecessary. Two options:

1. **Dev Container (Docker).** VS Code reopens the repo inside a container with a pinned Python, pytest, and the Python extension. Reproducible, isolated from the host, works offline once built. Cost: Docker Desktop on macOS.
2. **Plain venv.** `python -m venv` + `pip install pytest`. Lighter, but the host has Python 3.9.6, which is old (no `X | Y` type hints, no `match`), so we would want `uv` or pyenv for a newer one.

Plan: ship a `.devcontainer/` and keep the repo runnable without it (`make`/venv). Both use the same `leet` CLI and pytest tests.

## Problem format

One folder per problem, ordered by the NeetCode roadmap:

```
problems/
  arrays-hashing/
    001-contains-duplicate/
      README.md          statement, examples, constraints, hints
      solution.py        starter stub; the file the user edits
      tests.json         cases: [{"args": [...], "expected": ...}, ...]
      meta.json          id, title, category, difficulty, function name, comparison mode
```

Reference solutions live outside the problem folders (`reference/<id>.py`) so they are not spoiled by browsing. They exist to validate `tests.json`.

Shared harness in `leet/`:

- `ListNode`, `TreeNode`, `Node` (graph/random-pointer) helpers, plus builders and serializers so tests.json can describe them as plain lists.
- Comparison modes in `meta.json`: `exact`, `unordered` (any order of results), `unordered_nested`, `float_tolerance`, `custom` (for problems with multiple valid answers).
- Design-class problems (LRU Cache, Trie, etc.) use `ops` / `args` / `expected` sequences in `tests.json`.

## CLI: `leet`

| Command | What it does |
|---|---|
| `leet list [--category X] [--todo]` | List problems with status |
| `leet start <id\|slug>` | Open the problem's `solution.py` and `README.md` in VS Code (`code` command) |
| `leet test [<id>]` | Run visible tests, print pass/fail and the first failing case; defaults to the problem for the open file |
| `leet submit [<id>]` | Run all tests including hidden/edge cases, with a timeout; records the result |
| `leet progress` | Solved counts per category, streak, attempts |
| `leet reset <id>` | Restore the starter stub (asks first) |
| `leet next` | Suggest the next unsolved problem (optionally spaced-repetition review) |

Runs happen in a subprocess with a per-case timeout (default 5s) and, inside the container, a memory limit. Progress is stored in `progress.db` (SQLite) or `progress.json`, gitignored.

## VS Code integration

- `.vscode/tasks.json`: "Leet: test current file" and "Leet: submit current file" bound to keyboard shortcuts.
- pytest discovery so the Testing panel shows each case as a test.
- `.devcontainer/devcontainer.json` with the Python extension preinstalled.
- Optional later: a thin extension or CodeLens for Run/Submit above the function.

## Content pipeline

1. `data/neetcode150.json`: ordered list of titles, categories, difficulty.
2. For each problem, generate `README.md`, starter stub, `reference/<id>.py`, and `tests.json` (Claude drafts, human spot checks).
3. `leet validate`: runs every reference solution against its tests, and for problems where it matters, against a brute-force solution on randomized inputs. CI-style gate: a problem is not shippable until it validates.
4. Edge-case checklist per problem: empty input, single element, duplicates, max constraints (for TLE detection), negative numbers.

## Phases

1. **Skeleton + vertical slice:** `leet` CLI (`list`, `start`, `test`), harness, 5 problems from Arrays & Hashing, devcontainer, VS Code tasks.
2. **Full harness:** `submit`, progress DB, comparison modes, ListNode/TreeNode/design-class support.
3. **Content at scale:** generate and validate all 150, category by category.
4. **Extras:** spaced repetition, timer, notes per problem, solution write-ups (hidden until solved).

## Open questions

- Dev Container vs plain venv as the primary path?
- Reveal reference solutions after solving, or never ship them?
- Keep progress in-repo (gitignored) or in `~/.offline-leet`?
- Is a timer / interview-mode wanted in v1?

## Status

- Done: all 150 NeetCode problems, the web UI, the harness for lists, trees, graphs, intervals, design classes, in-place edits, and custom checkers (see `leet/structures.py`, `leet/runner.py`).
- Hidden tests (big inputs built on demand) exist for the problems listed by `leet list --hidden`; there is no separate submit step, they run with every test run.
- Not done: hidden tests for the other problems, timer, spaced repetition, written explanations for the reference solutions.
