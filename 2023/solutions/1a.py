
import os

from pathlib import Path

# Open file containing input
BASE_PATH = Path(__file__).parent.parent

data_file = f"1a.txt"
data_path = BASE_PATH / "inputs" / data_file

if not os.path.exists(data_path):
    raise ValueError(f"Unable to find {data_path} file!")

with open(data_path, "r") as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]

# Calculate number for first task
total = 0
for line in lines:
    line_numbers = "".join([c for c in line if c.isdigit()])
    if len(line_numbers) > 0:
        total += int(line_numbers[0] + line_numbers[-1])
print(total)
