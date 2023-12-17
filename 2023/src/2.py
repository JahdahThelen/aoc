import sys
import re
from src.utils import input


def a(file_name: str):
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

    return sum(possible_games)

def b():
    return "unknown"

def max_of_color(line: str, color: str) -> int:
    pattern = r"\d* " + color

    result = re.compile(pattern).findall(line)
    max_cubes = max([int(x.split()[0]) for x in result])
    return max_cubes

def main():
    return (a("2a.txt"), b())
