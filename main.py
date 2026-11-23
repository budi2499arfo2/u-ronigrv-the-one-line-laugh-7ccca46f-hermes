"""The One-Line Laugh — Hermes entry.

One funny line about the inbox: 1,204 unread emails, and the only one
marked urgent is a newsletter about AI inbox triage — the inbox
selling you the cure for the inbox. The semicolon keeps the punch
tight: the count, then the twist, nothing in between.
"""

import os
import sys

TEXT = "I have 1,204 unread emails; the only one marked urgent is a newsletter about AI inbox triage."

MAX_CHARS = 200


def main():
    text = TEXT
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: {len(text)} characters (must be 1-{MAX_CHARS})", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: text is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(text)} characters, verified byte-for-byte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
