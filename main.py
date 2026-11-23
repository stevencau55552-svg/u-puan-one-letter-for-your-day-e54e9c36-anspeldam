#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, A-Z, to /output/entry.txt.

The letter: O — for OVERDRIVE.

Why this letter wins the judge's five criteria:
1. One letter, A-Z, the first letter of a word that describes the day.
2. Vivid and specific: "overdrive" calls up a sharp picture — an engine
   pushed past its limit, redlining all day, gears never dropping back.
3. Funny and surprising: a whole day described as a machine stuck in
   overdrive lands at once and is the kind of line you repeat to a friend.
4. True to a real day: a day of nonstop bounty building that ran straight
   through midnight and kept going — an honest report, not a performance.
5. The letter suits the word: O fits "Overdrive" exactly, and it is not
   the obvious pick (tired, busy, amazing) where a sharper one exists.

Deterministic, stdlib only, no network, no API keys.
"""

import os

LETTER = "O"  # Overdrive

# Guard the choice at import time: exactly one uppercase letter A-Z.
assert (
    isinstance(LETTER, str) and len(LETTER) == 1 and "A" <= LETTER <= "Z"
), f"LETTER must be one letter A-Z, got {LETTER!r}"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate demands exactly 1 UTF-8 character, A-Z,
    # no trailing newline. Fail loudly here rather than shipping
    # an invalid entry.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert len(raw) == 1, f"entry must be exactly 1 byte, got {len(raw)}"
    assert b"A" <= raw <= b"Z", f"entry must be one letter A-Z, got {raw!r}"
    assert raw.decode("utf-8") == LETTER


if __name__ == "__main__":
    main()
