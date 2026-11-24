"""Funniest Time Machine Warning Label: writes one warning label to /output/entry.txt."""

from pathlib import Path

LINE = "WARNING: Do not operate while paradoxical. If you meet yourself, neither of you is the designated driver."


def main() -> None:
    # Gate: the entry must be 1-120 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 120 or not LINE.strip():
        raise ValueError("entry line must be 1-120 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
