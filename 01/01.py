import pathlib


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

summe = 0
for i, j in zip(sorted(col1), sorted(col2)):
    summe += max(i, j) - min(i, j)

print(summe)
