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
