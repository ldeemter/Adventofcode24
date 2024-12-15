from pathlib import Path
import re


def getDataLines():
    with open(Path(__file__).parent / "data.txt") as file:
        lines = file.readlines()
        return lines


grid = getDataLines()
aLocations = []
for j in range(len(grid)):
    aPositionsInLine = [m.start(0) for m in re.finditer("A", grid[j])]
    aLocations.extend([(i, j) for i in aPositionsInLine])


def getTopLeftBottomRightDiagonal(x, y):
    return grid[y - 1][x - 1] + grid[y][x] + grid[y + 1][x + 1]


def getBottomLeftToTopRightDiagonal(x, y):
    return grid[y - 1][x + 1] + grid[y][x] + grid[y + 1][x - 1]


possibleConfigurations = ["MAS", "SAM"]
counter = 0
for x, y in aLocations:
    if not (0 < y < len(grid) - 1 and 0 < x < len(grid[0]) - 1):
        continue
    if (
        getTopLeftBottomRightDiagonal(x, y) in possibleConfigurations
        and getBottomLeftToTopRightDiagonal(x, y) in possibleConfigurations
    ):
        counter += 1

print(counter)
