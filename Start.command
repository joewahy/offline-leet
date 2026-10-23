#!/bin/bash
# Double-click to start offline-leet. Needs no network.
cd "$(dirname "$0")" || exit 1
for py in .venv/bin/python python3.12 python3.13 python3.11 python3; do
  if command -v "$py" >/dev/null 2>&1; then
    exec "$py" -m leet serve
  fi
done
echo "Python 3.11+ not found. Install it once (needs internet), then run this again."
read -r -p "Press Enter to close"
