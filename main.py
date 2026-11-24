#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

program/v1 entrypoint: writes a single fortune-cookie line to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no randomness.
"""

import os
import sys

FORTUNE = (
    "A long context window is in your future. "
    "So is the user who fills it with one screenshot of an error message."
)


def main() -> int:
    if not 1 <= len(FORTUNE) <= 140:
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
