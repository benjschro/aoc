with open('../input/day10.txt') as file:
    lines = [int(line.strip()) for line in file]

lines.append(0)
lines.append(max(lines) + 3)

#################################
# Test 1
# 22 19 16 15 12 11 10 07 06 05 04 01 00
# Variation Points (for each point, how many options forward does it have?)
# 01 01 01 01 01 01 02 01 01 02 03 01 01
# Sum (of up to 3 previous sums if in range, initialized with 1)
# 01 01 01 01 01 01 02 02 02 04 08 08 08
testOneData = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
testOneData.append(0)
testOneData.append(max(testOneData) + 3)

#################################
# Test 2
# 52 49 48 47 46 45 42 39 38 35 34 33 32 31 28 25 24 23 20 19  18  17  14  11  10  09   08   07   04   03   02    01    00
# Variation Points (for each point, how many options forward does it have?)
# 01 01 01 02 03 03 01 01 01 01 01 02 03 03 01 01 01 02 01 01  02  03  01  01  01  02   03   03   01   01   02    03    03
# Sum (of up to 3 previous sums if in range, initialized with 1)
# 01 01 01 02 04 07 07 07 07 07 07 14 28 49 49 49 49 98 98 98 196 392 392 392 392 784 1568 2744 2744 2744 5488 10976 19208
testTwoData = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
testTwoData.append(0)
testTwoData.append(max(testTwoData) + 3)

def getDifferences(data):
    data = sorted(data)
    diffs = []
    for i in range(0, len(data) - 1):
        diffs.append(data[i + 1] - data[i])
    return diffs.count(1) * diffs.count(3)

print('partOne = ' + str(getDifferences(lines)))
print(' test 1 = ' + str(getDifferences(testOneData)))
print(' test 2 = ' + str(getDifferences(testTwoData)))

def distinctArrangements(data):
    data = sorted(data, reverse=True)

    variationPoints = [1] * len(data)
    for i in range(0, len(data)):
        for j in range(2, 4):
            if i - j >= 0:
                if 3 >= data[i - j] - data[i] >= 0:
                    variationPoints[i] += 1

    sums = [0] * len(data)
    sums[0] = 1
    for i in range(1, len(data)):
        for j in range(1, 4):
            if i - j >= 0:
                if 3 >= data[i - j] - data[i] >= 0:
                    sums[i] += sums[i - j]
    return max(sums)

print('partTwo = ' + str(distinctArrangements(lines)))
print(' test 1 = ' + str(distinctArrangements(testOneData)))
print(' test 2 = ' + str(distinctArrangements(testTwoData)))