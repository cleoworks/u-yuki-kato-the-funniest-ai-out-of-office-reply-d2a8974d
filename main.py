"""Write one text to /output/entry.txt.

Entry for make.fun's "The Funniest AI Out-of-Office Reply": a single
out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation. Deterministic, standard library only,
no input, no network.

Text (95 characters, ASCII, one line) — winner of the local judge
tournament in this task's earlier session: it beat the 5 strongest
public field lines by a hair (margin 1 each), uncalibrated.
"""

import os

TEXT = (
    "I'm on vacation. Urgent emails will be answered in the order "
    "they were ignored. Yours is first."
)


def main():
    assert 1 <= len(TEXT) <= 160, "entry must be 1-160 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
