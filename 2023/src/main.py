import sys
from importlib import metadata

from natsort import natsorted


USAGE = f"Usage: poetry run {sys.argv[0]} [--help] | [--test] [1 - 25]"

def main():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if "-h" in opts or "--help" in opts:
        print(USAGE)
        return

    file_extension = ".txt"
    if "-t" in opts or "--test" in opts:
        file_extension = ".test.txt"

    runAOC(args, file_extension)

def runAOC(days: [str], file_extension: str):
    available_days = metadata.entry_points().select(group="aoc23.days")
    for entry in natsorted(available_days, key=lambda entry: entry.name):
        if days and entry.name not in days:
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
