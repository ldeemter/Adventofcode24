from pathlib import Path
import re


def getDataLines():
    with open(Path(__file__).parent / "data.txt") as file:
        lines = file.read()
        return lines


data = getDataLines()

operations = re.findall(r"mul\((\d+)\,(\d+)\)", data)
total = 0
for i, j in operations:
    total += int(i) * int(j)
print(total)
