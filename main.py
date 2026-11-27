#!/usr/bin/env python3
import os

TEXT = (
    "Snoozelag: the groggy gap between what your alarm stopped and what "
    "your body still believes. Named for the snooze button's five-minute "
    "lie, sold as rest."
)

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
