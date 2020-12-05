with open('../input/day5.txt') as file:
    lineArray = [line.strip() for line in file]

highestID = 0
idList = []
for line in lineArray:
    seatID = 0
    for i, char in enumerate(line):
        if char == 'B':
            seatID += 8 * (1 << (6 - i))
        elif char == 'R':
            seatID += (1 << (9 - i))

    idList.append(seatID)
    highestID = max(highestID, seatID)

mySeat = 0
for id in sorted(idList):
    if id + 1 not in idList:
        mySeat = id + 1
        break

print('partOne = ' + str(highestID))
print('partTwo = ' + str(mySeat))

# $ python3 day5.py
# partOne = 866
# partTwo = 583