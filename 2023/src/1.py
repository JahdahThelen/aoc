import sys
from src.utils import input


def a(file_name: str):
    total = 0

    for line in input(file_name):
        line = line.replace("\n", "")
        line_numbers = "".join([c for c in line if c.isdigit()])
        if len(line_numbers) > 0:
            total += int(line_numbers[0] + line_numbers[-1])

    return total

def b():
    return "unknown"

def main():
    solution_a = a("1a.txt")
    solution_b = b()
    print(f"Day 1: a {solution_a}, b {solution_b}")
