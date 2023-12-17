import sys
from src.utils import input


def a(file_name: str):
    total = 0

    for line in input(file_name):
        winning_numbers = [int(c) for c in line.split(":")[1].split("|")[0].split()]
        card_numbers = [int(c) for c in line.split(":")[1].split("|")[1].split()]

        matching_numbers = [num for num in card_numbers if num in winning_numbers]

        if len(matching_numbers) == 1:
            total += 1
        elif len(matching_numbers) > 1:
            total += 2 ** (len(matching_numbers) - 1)

    return total

def b():
    return "unknown"

def main():
    return (a("4a.txt"), b())
