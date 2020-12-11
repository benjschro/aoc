with open('../input/day8.txt') as file:
    lines = [line.strip() for line in file]

partOneSum = partTwoSum = skip = 0
for line in lines:

    countPartOne = 0
    countPartTwo = 2
    for idx, c in enumerate(line):
        if idx != 0 and idx != len(line) - 1:
            if skip == 0:
                if c in ['\\', '\"']:
                    if line[idx + 1] == 'x':
                        skip = 3
                    else:
                        skip = 1
                countPartOne += 1
            else:
                skip -= 1

        if c in ['\\', '\"']:
            countPartTwo += 2
        else:
            countPartTwo += 1

    partOneSum += len(line) - countPartOne
    partTwoSum += countPartTwo - len(line)

print('partOne = ' + str(partOneSum))
print('partTwo = ' + str(partTwoSum))

# $ python day8.py
# partOne = 1333
# partTwo = 2046