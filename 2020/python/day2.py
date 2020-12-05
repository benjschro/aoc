import re

with open('../input/day2.txt') as file:
    myList = [line.strip() for line in file]

partOne = 0
partTwo = 0

stringPattern = '^(.*)-(.*) (.): (.*)$'
for line in myList:
    m = re.match(stringPattern, line)
    minNum = int(m.group(1))
    maxNum = int(m.group(2))
    reqChar = m.group(3)
    password = m.group(4)

    if minNum <= password.count(reqChar) <= maxNum:
        partOne = partOne + 1

    if (password[minNum - 1] == reqChar) != (password[maxNum - 1] == reqChar):
        partTwo = partTwo + 1

print("partOne = " + str(partOne))
print("partTwo = " + str(partTwo))

# $ python3 day2.py
# partOne = 546
# partTwo = 275