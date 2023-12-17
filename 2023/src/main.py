import sys
from importlib import metadata

from natsort import natsorted


def main():
    names = sys.argv[1:]
    days = metadata.entry_points().select(group="aoc23.days")
    for entry in natsorted(days, key=lambda entry: entry.name):
        if names and entry.name not in names:
            continue
        a = "unknown"
        b = "unknown"
        try:
            day = entry.load()
            a = day.a(f"{entry.name}a.txt")
            b = day.b(f"{entry.name}b.txt")
        except (ModuleNotFoundError, AttributeError):
            pass
        finally:
            print(f"Day {entry.name:>{2}}:   a = {a:<{10}} b = {b:<{10}}")

if __name__ == "__main__":
    main()
