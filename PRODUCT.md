# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
The owner, a developer preparing for coding interviews by working through the NeetCode 150 in Python, in regular sessions (solve new problems, then review due ones). Often without reliable internet. Desktop-first; a phone layout exists as a secondary context.

## Product Purpose
Practice all 150 NeetCode problems in Python entirely on the user's own machine. A local web page (served by `python3 -m leet serve`) gives a statement, a code editor, a test runner with failure detail, hints, a reference solution with explanation, a performance comparison, a topic roadmap, and a spaced-repetition review schedule. The same problems also run from the `leet` CLI and VS Code. Success is steady daily practice with solutions retained over time.

## Positioning
Fully offline and private: no account, no network after setup, no telemetry, and no CDNs or runtime downloads (the Monaco editor is vendored). Progress and solutions stay on disk in the repo.

## Operating Context
- Launched by double-clicking `Start.command` or running `python3 -m leet serve`; opens `http://localhost:8765`. Python 3.11+ required, nothing else.
- Solutions are plain `solution.py` files per problem, tracked in git; progress lives in a gitignored `progress.json`.
- Problems are ordered by the NeetCode roadmap in 18 categories, from Arrays & Hashing to Bit Manipulation.
- Review schedule: solved problems return after 1, 3, 7, 14, then 30 days.
- Also usable via CLI (`leet list/next/start/test/reset/perf/serve/validate`) and VS Code tasks, plus a Dev Container.

## Capabilities and Constraints
- Web UI: problems list with solved/attempted/due marks, search and All/To do/Due filters, a next-problem jump, Monaco editor with autosave, Run (Cmd/Ctrl+Enter), resizable panes, three tiered hints on Medium/Hard problems, reference Solution (gated behind a confirm until solved), Compare with reference, Reset (backs up first), Roadmap topic map with a streak and activity heatmap, custom test cases checked against the reference, personal notes, light and dark themes, phone layout with statement/editor/results tabs.
- No network dependency may be introduced: no CDN assets, web fonts, analytics, or runtime downloads.
- Timeouts rely on Unix signals, so macOS and Linux only; user code runs unsandboxed.
- Statements, tests, hints, and reference solutions are original, not copied from LeetCode.
- Hidden tests exist for 58 problems; there is no timer yet.

## Evidence on Hand
Real content throughout: 150 problems under `problems/`, reference solutions under `reference/`, a built web UI under `leet/web/`. No testimonials, users, or metrics exist; none should be invented.

## Product Principles
- Offline-first and private is non-negotiable: every feature must work with the network off.
- Honest feedback over reassurance: failures show input, expected, actual, and output; performance verdicts state their limits.
- Protect the learner's effort: solutions are not spoiled before they are earned, and the user's code is never destroyed (backups before reset).
- Plain files over hidden state: solutions and problems stay readable and editable in the repo.
- Built for repeated daily use: low friction to start, and the next thing to do is always obvious.

## Accessibility & Inclusion
Target WCAG 2.1 AA. Respect `prefers-reduced-motion`. Keyboard operable (shortcuts, resizable dividers with arrow keys). Phone layout must stay usable.
