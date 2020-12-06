import re

with open('../input/day7.txt') as file:
    instructions = [line.strip() for line in file]

wires = {}

pattern = '^(.*) -> (.*)$'
skipList = []
partTwoActive = False
partOneAnswer = 0
partTwoAnswer = 0
for loop in range(2):
    while len(skipList) != len(instructions):
        for i, instruction in enumerate(instructions):
            if i not in skipList:
                m = re.match(pattern, instruction, re.I)
                dst = m.group(2)
                command = m.group(1).split()

                if len(command) == 1:
                    if command[0].isnumeric():
                        if partTwoActive and dst == 'b':
                            wires[dst] = partOneAnswer
                        else:
                            wires[dst] = int(command[0])
                        skipList.append(i)
                    else:
                        if command[0] in wires:
                            wires[dst] = wires[command[0]]
                            skipList.append(i)
                elif len(command) == 2:
                    if command[1] in wires:
                        wires[dst] = ~wires[command[1]]
                        skipList.append(i)
                elif len(command) == 3:
                    lside = None
                    if command[0].isnumeric():
                        lside = int(command[0])
                    else:
                        if command[0] in wires:
                            lside = wires[command[0]]
                    
                    rside = None
                    if command[2].isnumeric():
                        rside = int(command[2])
                    else:
                        if command[2] in wires:
                            rside = wires[command[2]]

                    if lside is not None and rside is not None:
                        if command[1] == 'AND':
                            wires[dst] = lside & rside
                            skipList.append(i)
                        elif command[1] == 'OR':
                            wires[dst] = lside | rside
                            skipList.append(i)
                        elif command[1] == 'LSHIFT':
                            wires[dst] = lside << rside
                            skipList.append(i)
                        elif command[1] == 'RSHIFT':
                            wires[dst] = lside >> rside
                            skipList.append(i)
    if loop == 0:
        partTwoActive = True
        partOneAnswer = wires['a']
        wires.clear()
        skipList.clear()
    elif loop == 1:
        partTwoAnswer = wires['a']

print('partOne = ' + str(partOneAnswer))
print('partTwo = ' + str(partTwoAnswer))

# $ python day7.py
# partOne = 956
# partTwo = 40149