import sys
import re
from utils import input


def main(file_name: str):
    possible_games = []
    impossible_games = []
    game = 1

    for line in input(file_name):
        if (
            max_of_color(line, "red") <= 12
            and max_of_color(line, "green") <= 13
            and max_of_color(line, "blue") <= 14
        ):
            possible_games.append(game)
        else:
            impossible_games.append(game)

        game += 1

    print(f"Possible: {possible_games}")
    print(f"Impossible: {impossible_games}")
    print(f"Sum of possible: {sum(possible_games)}")


def max_of_color(line: str, color: str) -> int:
    pattern = r"\d* " + color

    result = re.compile(pattern).findall(line)
    max_cubes = max([int(x.split()[0]) for x in result])
    return max_cubes


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        main("2a.txt")
    elif args[0] == "test":
        main("2a.test.txt")

