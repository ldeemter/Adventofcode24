from pathlib import Path


def getDataLines():
    with open(Path(__file__).parent / "data.txt") as file:
        lines = file.readlines()
        return lines


class Report:
    def __init__(self, levels: list[int]) -> None:
        self.levels = levels

    def isSafe(self):
        isAscending = self.levels[0] < self.levels[1]
        for i in range(1, len(self.levels)):
            diff = max(self.levels[i - 1], self.levels[i]) - min(
                self.levels[i - 1], self.levels[i]
            )
            if not 0 < diff < 4:
                return False
            if isAscending:
                if not self.levels[i - 1] < self.levels[i]:
                    return False
            else:
                if not self.levels[i - 1] > self.levels[i]:
                    return False
        return True

    @classmethod
    def createFromLine(cls, line: str):
        return cls(list(map(int, line.split())))


reports = getDataLines()
print(sum([Report.createFromLine(line).isSafe() for line in reports]))
