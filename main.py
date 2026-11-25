"""One-line entry: The Meeting That Should Have Been an Email.

Writes a single joke line to /output/entry.txt, after checking it
against the same gate the bounty scorer applies: UTF-8 text, 1 to
200 characters, not only white space, and a single line.
"""

import os

LINE = "We spent an hour deciding the next meeting should have been an email, then scheduled it anyway."


def validate(text):
    """Mirror the bounty gate. Raise ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
