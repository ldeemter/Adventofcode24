from itertools import combinations
from pathlib import Path


def getDataLines():
    with open(Path(__file__).parent / "data.txt") as file:
        lines = file.readlines()
        return lines


class Report:
    def __init__(self, levels: list[int]) -> None:
        self.levels = levels

    def _isSafe(self, levels: list[int]):
        isAscending = levels[0] < levels[1]
        for i in range(1, len(levels)):
            diff = max(levels[i - 1], levels[i]) - min(levels[i - 1], levels[i])
            if not 0 < diff < 4:
                return False
            if isAscending:
                if not levels[i - 1] < levels[i]:
                    return False
            else:
                if not levels[i - 1] > levels[i]:
                    return False
        return True

    def isSafe(self):
        if self._isSafe(self.levels):
            return True
        else:
            for levelWithOneRemoved in combinations(self.levels, len(self.levels) - 1):
                if self._isSafe(levelWithOneRemoved):
                    return True
        return False

    @classmethod
    def createFromLine(cls, line: str):
        return cls(list(map(int, line.split())))


reports = getDataLines()
print(sum([Report.createFromLine(line).isSafe() for line in reports]))
