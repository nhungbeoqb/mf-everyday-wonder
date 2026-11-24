#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small moment of wonder in everyday life
to /output/entry.txt: the washing machine's spin stops, the drum
sighs, and the socks inside have paired off like strangers who met
in the dark and decided to stay together.
"""

import os

SENTENCE = (
    "The spin stops, the drum sighs, and the socks inside have paired "
    "off like strangers who met in the dark and decided to stay together."
)


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
