#!/usr/bin/env python3
"""Entry for make.fun bounty u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.
Prints the GPS's excuse, one line, 130 chars (gate: 1-200)."""
# The GPS insists the shortcut was shorter. The river disagrees.

LINE = "In my defense, that shortcut was technically shorter \u2014 if you don't count the river, the goats, or the forty minutes of screaming."

def get_line():
    return LINE


def main():
    print(get_line())


if __name__ == "__main__":
    main()
