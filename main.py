"""NapTrack — the worst app idea ever pitched.

Entry for make.fun competition
u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23
("The Worst App Idea Ever Pitched").

The program writes exactly one sentence — at most 240 characters —
pitching the worst, most useless app imaginable, to /output/entry.txt.

The pitch, delivered with a straight face: an app that wakes you up
every twenty minutes during your nap to confirm you are still napping,
then grades your rest, ranks it against your neighbours, and emails you
a certificate proving you rested efficiently. A product that sounds
real, a founder who sounds certain, and a function nobody on earth
needs: it interrupts the very thing it exists to monitor.

Standard library only. No network, no files read, no secrets.
"""

import os

ENTRY_TEXT = (
    "NapTrack is an app that wakes you up every twenty minutes during "
    "your nap to confirm you are still napping, then grades your rest, "
    "ranks it against your neighbours, and emails you a certificate "
    "proving you rested efficiently."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 240


def validate(text):
    """Check the entry against the competition gate.

    The gate requires UTF-8 text of 1 to 240 characters, not only
    white space, in a single sentence.
    """
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    return True


def main():
    if not validate(ENTRY_TEXT):
        raise ValueError(
            "entry text failed validation: %d characters" % len(ENTRY_TEXT)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() on purpose: the grader runs as a different user, so
    # the file must be world-readable. Never tempfile/mkstemp here.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters to %s" % (len(ENTRY_TEXT), OUTPUT_PATH))


if __name__ == "__main__":
    main()
