#!/usr/bin/env python3
"""Write the one-star houseplant review to the output file.

Stdlib only, deterministic: the same line is written on every run.
The output path honours MAKEFUN_OUTPUT_DIR when set, else
/output/entry.txt. The gate (1-279 characters, not only whitespace)
is asserted before writing.
"""

import os

REVIEW = (
    "One star: my owner waters me with leftover protein shake, "
    "calls me his 'little guy', and has moved me four times this "
    "month because I 'clash with the sofa'. The sofa now gets more "
    "sunlight than I do."
)


def main() -> None:
    text = REVIEW
    assert 1 <= len(text) <= 279, f"review is {len(text)} chars, outside 1-279"
    assert text.strip(), "review must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
