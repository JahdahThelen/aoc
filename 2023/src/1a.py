from utils import input


total = 0

for line in input("1a.txt"):
    line = line.replace("\n", "")
    line_numbers = "".join([c for c in line if c.isdigit()])
    if len(line_numbers) > 0:
        total += int(line_numbers[0] + line_numbers[-1])

print(total)
