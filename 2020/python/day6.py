with open('../input/day6.txt') as file:
    lineArray = [line.strip() for line in file]

partOneSum = partTwoSum = 0

tmpDict = {}

loop = 0
for i, line in enumerate(lineArray):
    if len(line) != 0:
        for c in line:
            if c not in tmpDict:
                tmpDict[c] = 1
            else:
                tmpDict[c] += 1
        loop += 1

    if len(line) == 0 or i == len(lineArray) - 1:
        for item in tmpDict:
            partOneSum += 1
            if tmpDict[item] == loop:
                partTwoSum += 1
        loop = 0
        tmpDict.clear()

print('partOne = ' + str(partOneSum))
print('partTwo = ' + str(partTwoSum))

# $ python day6.py
# partOne = 6335
# partTwo = 3392