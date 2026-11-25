"""Pigeon Pitch, One Line — a city pigeon's elevator pitch to investors.

The program writes exactly one line of English text (166 characters,
within the 200-character gate) to entry.txt in the harness output
directory. Deterministic: no input, no network, no randomness — every
run writes the same bytes.
"""

import os

PITCH = (
    "Investors, I run Coo.ly \u2014 the Uber for breadcrumbs: 40 million "
    "pigeons, zero drivers, and every statue downtown is already our "
    "billboard. Seed round? One bag of seed."
)


def main() -> None:
    # Gate mirror: the sealed scorer requires 1-200 chars, non-blank,
    # single line. Fail loudly here rather than shipping a bad entry.
    assert PITCH.strip(), "pitch must not be blank"
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert "\n" not in PITCH and "\r" not in PITCH, \
        "pitch must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)
    # Mirror to /output when the harness points elsewhere, best effort.
    if os.path.abspath(output_dir) != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8",
                      newline="\n") as f:
                f.write(PITCH)
        except OSError:
            pass


if __name__ == "__main__":
    main()
