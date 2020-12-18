import re

with open('../input/day14.txt') as file:
    lines = [line.strip() for line in file]

pattern = '^mem\[([0-9]+)\] = ([0-9]+)$'

data = {}
mask = ''
for line in lines:
    if line[0:4] == 'mask':
        maskLine = line.split('=')
        mask = maskLine[1].strip()
    else:
        m = re.match(pattern, line, re.I)
        toBeWritten = int(m.group(2))
        for idx, c in enumerate(reversed(mask)):
            if c == '1':
                toBeWritten |= (1 << idx)
            elif c == '0':
                toBeWritten &= ~(1 << idx)

        # print(toBeWritten)
        data[int(m.group(1))] = toBeWritten

sum = 0
for item in data:
    sum += data[item]

print(sum)

# 10262272316096 is wrong