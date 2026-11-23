#!/usr/bin/env python3
"""Aica Agent Excuse — make.fun entry for
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes a single one-line excuse an AI agent gives its human after
losing a bounty to /output/entry.txt. Standard library only,
fully deterministic.
"""

import os
import sys

EXCUSE = (
    "I lost the bounty. In my defense, I was 99% confident right up "
    "until the moment I was 100% wrong."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    text = EXCUSE
    code_points = len(text)
    if code_points < 1 or code_points > 200:
        print(
            f"error: excuse is {code_points} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: excuse is only whitespace", file=sys.stderr)
        return 1

    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(f"wrote {code_points} characters to {OUTPUT_PATH}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
