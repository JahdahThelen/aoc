import sys
from utils import input


def main(file_name: str):
    total = 0

    for line in input(file_name):
        line = line.replace("\n", "")
        line_numbers = "".join([c for c in line if c.isdigit()])
        if len(line_numbers) > 0:
            total += int(line_numbers[0] + line_numbers[-1])

    print(total)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        main("1a.txt")
    elif args[0] == "test":
        main("1a.test.txt")
