"""Write the one-letter bounty entry: a single letter A to Z."""

import os
from pathlib import Path

LETTER = "Q"

FILENAME = "entry.txt"


def check(letter):
    """Return the entry as one uppercase letter, or exit with the reason."""
    cleaned = letter.strip().upper()
    if not cleaned:
        raise SystemExit(
            "LETTER is empty: set it to exactly one character A to Z"
        )
    if len(cleaned) != 1:
        raise SystemExit(
            "LETTER must be exactly one character, got %d: %r"
            % (len(cleaned), letter)
        )
    if not cleaned.isalpha():
        raise SystemExit("LETTER must be a letter, got %r" % (letter,))
    return cleaned


def destination():
    """Create the output directory if needed and return the file path."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or Path.cwd())
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / FILENAME


def main():
    letter = check(LETTER)
    path = destination()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(letter + "\n")
    print("wrote %r to %s" % (letter + "\n", path))


if __name__ == "__main__":
    main()
