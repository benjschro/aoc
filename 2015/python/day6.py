import re

with open('../input/day6.txt') as file:
    instructions = [line.strip() for line in file]

pattern = '^(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$'

partOneLights = {}
partTwoLights = {}
for instruction in instructions:
    m = re.match(pattern, instruction, re.I)
    command = m.group(1)
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2 = int(m.group(4))
    y2 = int(m.group(5))

    for i in range(x1, x2):
        for j in range(y1, y2):
            if (i, j) not in partOneLights:
                partOneLights[i, j] = 0

            if (i, j) not in partTwoLights:
                partTwoLights[i, j] = 0

            if command == 'turn on':
                partOneLights[i, j] = 1
                partTwoLights[i, j] += 1
            elif command == 'turn off':
                partOneLights[i, j] = 0
                partTwoLights[i, j] = max(0, partTwoLights[i, j] - 1)
            elif command == 'toggle':
                partOneLights[i, j] ^= 1
                partTwoLights[i, j] += 2

partOneSum = 0
for entry in partOneLights:
    if partOneLights[entry] == 1:
        partOneSum += 1

partTwoSum = 0
for entry in partTwoLights:
    partTwoSum += partTwoLights[entry]

print('partOne = ' + str(partOneSum)) #569999, 17836115
print('partTwo = ' + str(partTwoSum))