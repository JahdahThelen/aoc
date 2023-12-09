import sys
from utils import input


def main(file_name: str):
    print("This task has not been completed!")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        main("3a.txt")
    elif args[0] == "test":
        main("3a.test.txt")

