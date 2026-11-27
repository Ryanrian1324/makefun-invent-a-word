#!/usr/bin/env python3
import pathlib, os

SNOOZE_LINES = (
    "Snoozelag: the groggy gap between what your alarm stopped and what ",
    "your body still believes. Named for the snooze button's five-minute ",
    "lie, sold as rest. Everyone pays it; nobody admits it in writing, out loud.",
)

def main():
    destination = pathlib.Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("".join(SNOOZE_LINES), encoding="utf-8")

if __name__ == "__main__":
    main()
