with open('../input/day1.txt') as file:
    input = file.readline()

floor = 0
position = 1
enteredBasementPosition = 0
for instruction in input:
    if instruction == '(':
        floor += 1
    elif instruction == ')':
        floor -= 1
    if floor == -1 and enteredBasementPosition == 0:
        enteredBasementPosition = position
    position += 1

print('partOne = ' + str(floor))
print('partTwo = ' + str(enteredBasementPosition))

# $ python3 day1.py
# partOne = 74
# partTwo = 1795