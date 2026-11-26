#!/usr/bin/env python3
"""Rename the Planet — one funny new name for a planet, plus the why.

The entry is a single line, under 200 characters, that renames Neptune
and earns the name from Neptune's own trait: its 165-year orbit, the
slowest lap in the solar system. The joke is the idea — a planet that
takes a century and a half to circle back — not a pun on its name.
"""

import os
import stat
import sys

# The entry line. Neptune: 165 years per orbit around the Sun.
ENTRY = (
    "Neptune is now The Slow Reply \u2014 it takes 165 years to orbit "
    "the Sun and still leaves you on read."
)

MAX_CHARS = 200


def validate(text):
    """Gate mirror: UTF-8, 1-200 chars, not whitespace-only."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char cap" % len(text))
    text.encode("utf-8")  # raises if not encodable
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    line = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read back and confirm the file on disk is exactly the validated line.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise RuntimeError("entry.txt on disk does not match the validated line")
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
