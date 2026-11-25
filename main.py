#!/usr/bin/env python3
"""Funniest one-line out-of-office reply.

Writes a single original out-of-office auto-reply line to stdout and to
/output/entry.txt (creating /output if needed).
"""

import os
import sys

LINE = "I'm away until Monday. My inbox is home alone and has already eaten two urgent emails \u2014 send snacks, not deadlines."


def main() -> int:
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
