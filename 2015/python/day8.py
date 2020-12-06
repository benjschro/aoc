import re

with open('../input/day8.txt') as file:
    lines = [line.strip() for line in file]

partOneSum = 0
partTwoSum = 0
pattern = '^\"(.*)\"$'
for line in lines:
    m = re.match(pattern, line, re.I)
    lineDecoded = bytes(m.group(1), 'utf-8').decode('unicode_escape')
    partOneSum += len(line) - len(lineDecoded)

    count = 2
    for c in line:
        if c in ['\\', '\"']:
            count += 2
        else:
            count += 1
    
    partTwoSum += count - len(line)

print('partOne = ' + str(partOneSum))
print('partTwo = ' + str(partTwoSum))

# $ python day8.py
# partOne = 1333
# partTwo = 2046