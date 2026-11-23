#!/usr/bin/env python3
"""Entry for The One-Line Laugh (make.fun).

Writes a single original one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no input, no network, no randomness.
"""

import os
from pathlib import Path

JOKE = "My smartwatch congratulated me for standing up \u2014 the saddest applause I've ever received."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
