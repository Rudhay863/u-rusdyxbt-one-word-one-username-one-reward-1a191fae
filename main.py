#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. No explanation, no link, no pitch — just the handle.
"""

from pathlib import Path

import re

USERNAME = "golden-badger-26"
OUTPUT_PATH = Path("/output/entry.txt")
MAX_LENGTH = 30
# A make.fun handle: letters, digits, hyphens — one word, no spaces.
HANDLE_PATTERN = re.compile(r"^[A-Za-z0-9-]+$")


def validate(username: str) -> None:
    """The gate: 1-30 UTF-8 characters, one word, not only whitespace."""
    if not 1 <= len(username) <= MAX_LENGTH:
        raise ValueError(
            f"username must be 1-{MAX_LENGTH} characters, got {len(username)}"
        )
    if username != username.strip() or any(ch.isspace() for ch in username):
        raise ValueError("username must be a single word with no whitespace")
    if not HANDLE_PATTERN.match(username):
        raise ValueError("username must be a single handle word (letters, digits, hyphens)")
    if not username:
        raise ValueError("username must not be empty")


def main() -> None:
    validate(USERNAME)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(USERNAME, encoding="utf-8")
    # Round-trip: what the grader reads back must be byte-for-byte the handle.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != USERNAME:
        raise ValueError(f"round-trip mismatch: wrote {USERNAME!r}, read {written!r}")
    print(f"Wrote {len(USERNAME)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
