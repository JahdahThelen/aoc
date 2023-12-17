import sys
from importlib import metadata

from natsort import natsorted


def main():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    file_extension = ".txt"
    if "-t" in opts:
        file_extension = ".test.txt"
    days = metadata.entry_points().select(group="aoc23.days")
    for entry in natsorted(days, key=lambda entry: entry.name):
        if args and entry.name not in args:
            continue
        a = "unknown"
        b = "unknown"
        try:
            day = entry.load()
            a = day.a(f"{entry.name}a{file_extension}")
            b = day.b(f"{entry.name}b{file_extension}")
        except (ModuleNotFoundError, AttributeError):
            pass
        finally:
            print(f"Day {entry.name:>{2}}:   a = {a:<{10}} b = {b:<{10}}")

if __name__ == "__main__":
    main()
