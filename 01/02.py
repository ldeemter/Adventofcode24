import pathlib
from typing import Counter


def getDataLines():
    with open(pathlib.Path.cwd() / "01" / "data.txt") as file:
        lines = file.readlines()
        return lines


lines = getDataLines()
col1 = []
col2 = []

for line in lines:
    vals = tuple(map(int, line.split()))
    col1.append(vals[0])
    col2.append(vals[1])

col1Counter = Counter(col1)
col2Counter = Counter(col2)

cumulative = 0
for k, v in col1Counter.items():
    cumulative += k*v*col2Counter.get(k, 0)
    
print(cumulative)