"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os


def main():
    line = (
        "That dead end was a shortcut \u2014 it cut three minutes off your "
        "trip by skipping the part where you actually arrive."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
