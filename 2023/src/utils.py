import os
from pathlib import Path

BASE_PATH = Path(__file__).parent

def input(file_name: str):

    file_path = BASE_PATH / "inputs" / file_name

    if not os.path.exists(file_path):
        raise ValueError(f"Unable to find {file_path} file!")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "")
            yield line
