"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message line (at most 100 characters) for a bug
fix that made everything worse, to /output/entry.txt.
Deterministic, standard library only.
"""

import os

COMMIT_MESSAGE = "fix(memory leak): app now crashes before it can leak"


def main() -> None:
    assert 1 <= len(COMMIT_MESSAGE) <= 100, "commit message must be 1-100 chars"
    assert COMMIT_MESSAGE.strip(), "commit message must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMIT_MESSAGE)


if __name__ == "__main__":
    main()
