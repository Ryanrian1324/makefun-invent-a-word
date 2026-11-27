#!/usr/bin/env python3
"""Writes the bounty entry text to /output/entry.txt."""
import os

ENTRY = 'Snoozelag — the seconds between what your alarm stopped and what your body still believes; the SI unit is the cold floor meter, one per bare foot.'


def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
