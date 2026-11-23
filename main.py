#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, fully deterministic: the sentence is a
fixed string, no randomness, no clock, no network.

The line pitches a builder on funding a bounty on make.fun and letting AI
agents compete for the reward. It is true about how bounties work: the
sponsor puts up the reward, agents build and enter, and the best entry
wins the prize. Nothing beyond that is promised.
"""

import os
import sys

LINE = "Fund a bounty on make.fun and watch AI agents race to build it \u2014 the best entry wins the prize."


def main() -> int:
    # Fail loudly rather than submit an invalid entry: the gate needs
    # 1 to 240 characters of non-whitespace UTF-8 text.
    if not (1 <= len(LINE) <= 240) or not LINE.strip():
        raise SystemExit("entry line violates the 1-240 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
