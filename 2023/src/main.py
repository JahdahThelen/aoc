import sys
from importlib import metadata

from natsort import natsorted


def main():
    names = sys.argv[1:]
    days = metadata.entry_points().select(group="aoc23.days")
    for entry in natsorted(days, key=lambda entry: entry.name):
        if names and entry.name not in names:
            continue
        day = entry.load()
        (a, b) = day()
        print(f"Day {entry.name}: a {a}, b {b}")
        print()

if __name__ == "__main__":
    main()
