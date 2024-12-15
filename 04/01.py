from pathlib import Path
import re


def getDataLines():
    with open(Path(__file__).parent / "data.txt") as file:
        lines = file.readlines()
        return lines


grid = getDataLines()
xLocations = []
for j in range(len(grid)):
    xPositionsInLine = [m.start(0) for m in re.finditer("X", grid[j])]
    xLocations.extend([(i, j) for i in xPositionsInLine])


def getNextPositions(x, y, verticalDirection, horizontalDirection):
    if horizontalDirection:
        xPositions = list(range(x, x + horizontalDirection * 4, horizontalDirection))
        for xPos in xPositions:
            if not 0 <= xPos < len(grid[0]):
                return None
    else:
        xPositions = [x] * 4

    if verticalDirection:
        yPositions = list(range(y, y + verticalDirection * 4, verticalDirection))
        for yPos in yPositions:
            if not 0 <= yPos < len(grid):
                return None
    else:
        yPositions = [y] * 4

    return [(y, x) for y, x in zip(yPositions, xPositions)]


def checkValidStrings(i, j):
    directions = [-1, 0, 1]
    validCount = 0
    for xDir in directions:
        for yDir in directions:
            if xDir == 0 and yDir == 0:
                continue
            if positions := getNextPositions(i, j, yDir, xDir):
                word = "".join(grid[i][j] for i, j in positions)
                if word == "XMAS":
                    validCount += 1
    return validCount


totalCount = 0
for i, j in xLocations:
    posCount = checkValidStrings(i, j)
    totalCount += posCount
print(totalCount)
