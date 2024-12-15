from pathlib import Path
import re


def getDataLines():
    with open(Path(__file__).parent / "data.txt") as file:
        lines = file.read()
        splitByDo = lines.split("do()")
        correctLines = []
        for i in splitByDo:
            splitByDonts = i.split("don't")
            correctLines.append(splitByDonts[0])
        return "".join(correctLines)


findNumberRegex = "d+"


data = getDataLines()

operations = re.findall(r"mul\((\d+)\,(\d+)\)", data)
total = 0
for i, j in operations:
    total += int(i) * int(j)
print(total)
