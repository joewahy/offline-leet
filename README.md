# offline-leet

Practice the NeetCode 150 offline, in Python, from VS Code. See [SPEC.md](SPEC.md) for the design.

## Setup (needs internet once)

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e '.[dev]'
```

Or open the folder in VS Code and choose "Reopen in Container" (uses `.devcontainer/`).

## Use

```bash
.venv/bin/leet list            # problems and status (--todo, --category)
.venv/bin/leet start 3         # open README + solution.py in VS Code
.venv/bin/leet test            # test the current problem (or pass an id/slug/path)
.venv/bin/leet validate        # check reference solutions against tests.json
```

In VS Code, run the task "Leet: test current file" (Terminal > Run Task, or bind a key to it) while a `solution.py` is open. Every case also appears in the Testing panel.

## Web UI (no commands needed)

Double-click `Start.command` (or run `leet serve`). Your browser opens `http://localhost:8765` with the problem list, statement, editor, and test results. Press Cmd+Enter to run. Your code autosaves to each problem's `solution.py`. Everything is served from this folder, so it works with no internet (for example, on a plane).

## The problem set

All 150 NeetCode problems are included, in roadmap order and grouped by category (Arrays & Hashing through Bit Manipulation). Starter code follows NeetCode's conventions: `ListNode`, `TreeNode`, `Node`, `Interval`, and the typing names (`Optional`, `List`, ...) are predefined, so you don't import them.

Problem statements and test cases are original (not copied from LeetCode). Each problem has hand-checked cases plus generated larger ones, including inputs big enough to make a naive solution time out. Problems with more than one valid answer (for example Course Schedule II) are checked by a validity checker rather than an exact match.

## Regenerating problems (for contributors)

Problems are defined in `tools/specs/*.py` and built with:

```bash
.venv/bin/python tools/build.py              # all categories (never overwrites your solution.py)
.venv/bin/python tools/build.py trees stack  # specific categories
.venv/bin/python tools/timing.py             # check that naive solutions time out on the big cases
```

`build.py` checks every reference solution against the hand-written cases, generates the larger cases, and cross-checks the reference against an independent brute-force solution on random small inputs.
