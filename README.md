# offline-leet

Practice all 150 NeetCode problems in Python with no internet. Everything runs on your machine: a local web page with a code editor, or the command line and VS Code if you prefer.

## Quick start

You need Python 3.11 or newer. Nothing else has to be installed, and nothing is downloaded when you run it.

Double-click `Start.command` (or run `python3 -m leet serve`). Your browser opens `http://localhost:8765`.

- Pick a problem from the **Problems** list (it shows solved and attempted marks).
- Read the statement on the left and write your solution in the editor on the right.
- Press **Run** or Cmd+Enter (Ctrl+Enter elsewhere). Failures show the input, the expected value, your output, any error, and anything you printed.
- Your code autosaves to the problem's `solution.py`.
- Stuck on a Medium or Hard problem? Click **Show hint** under the statement. There are three hints per problem, each more revealing than the last, and they stay hidden until you ask. Hints you have opened are remembered in your browser.

If macOS refuses to open `Start.command`, right-click it, choose Open, then Open again. Or run `python3 -m leet serve` in a terminal.

## Optional setup: the `leet` command and VS Code

The command line, pytest and the VS Code tasks use a virtual environment (needs internet once to install):

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e '.[dev]'
```

```bash
.venv/bin/leet list                # problems and status (--todo, --category <name>)
.venv/bin/leet start 3             # open the statement and solution.py in VS Code
.venv/bin/leet test                # test the current problem (or pass an id, slug or file path)
.venv/bin/leet serve               # start the web UI (--port, --no-open)
.venv/bin/leet validate            # check every reference solution against its tests
```

`leet start` needs the `code` command on your PATH (in VS Code: Shell Command: Install 'code' command in PATH).

In VS Code, open a `solution.py` and run the task **Leet: test current file** (Terminal > Run Task). Every test case also shows in the Testing panel. VS Code will underline `Optional`, `ListNode` and similar names in the starter code as undefined, because they are provided when the tests run (see below). It does not affect running.

There is also a Dev Container (`.devcontainer/`) if you want a pinned Python and your code isolated from the rest of your machine.

## The problems

All 150 NeetCode problems, in roadmap order, in 18 categories from Arrays & Hashing to Bit Manipulation:

```
problems/<category>/<id>-<slug>/
  README.md      the statement
  solution.py    your code (starter code to begin with)
  tests.json     test cases
  meta.json      title, difficulty, method name, how to compare results
reference/       reference solutions (spoilers!)
```

The starter code follows NeetCode's conventions. `ListNode`, `TreeNode`, `Node`, `Interval` and the typing names (`Optional`, `List`, `Dict`, ...) are already defined, so you do not import them. Each stub shows the class definition in a comment, as NeetCode does.

Other notes:

- Statements and tests are original, not copied from LeetCode. Some examples use the same well-known inputs.
- The 122 Medium and Hard problems have three tiered hints (`hints.json`). In the web UI they are revealed one at a time. In the problem's `README.md` they sit in a collapsed "Hints" section at the bottom (open it in VS Code's Markdown preview or on GitHub), so the statement itself stays spoiler-free. Easy problems keep a short, always-visible Hints section.
- Each problem has hand-written cases plus larger generated ones. Where several answers are valid (Course Schedule II, Alien Dictionary, Gas Station and others), a checker verifies the answer instead of comparing to one exact value.
- Design problems (LRU Cache, Twitter, Trie and others) are tested with a sequence of method calls and their expected results.
- Each case has a time limit of 5 seconds, and a run stops at the first timeout.
- `solution.py` files are tracked by git, so your solutions are committed along with everything else.

## Limitations

- The large test cases have at most about 10,000 elements, to keep the repo small. A slow solution (for example O(n^2)) can still pass on a fast machine, so these tests are weaker than LeetCode's at catching inefficiency.
- Your code runs as a normal process on your machine, with no sandbox and no memory limit. Use the Dev Container if that matters to you.
- Timeouts rely on Unix signals, so macOS and Linux work but Windows does not.
- Hints are static text, so they cannot react to your code. There is also no hidden-test submit step, reset-to-starter button, or timer yet.

## Regenerating problems (for contributors)

Problems are defined in `tools/specs/*.py`. Each defines the statement, starter code, a reference solution, hand-written cases, a generator for larger cases, and optionally a brute-force solution.

```bash
.venv/bin/python tools/build.py                 # build every category (never overwrites your solution.py)
.venv/bin/python tools/build.py trees stack     # build specific categories
.venv/bin/python tools/timing.py                # see which brute-force solutions time out on the big cases
.venv/bin/python tools/hintlib.py               # re-apply hints and list Medium/Hard problems without any
```

Hints live in `tools/hints/<category>.py` as `{problem_id: [hint1, hint2, hint3]}`, and `build.py` re-applies them after every build.

`build.py` checks each reference solution against the hand-written cases, generates the larger cases, and cross-checks the reference against the brute-force solution on random small inputs. The build stops at the first problem that fails a check.

See [SPEC.md](SPEC.md) for the design notes.
