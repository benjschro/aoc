counted = {}

def checkThenAddCoord(x, y):
    if (x,y) in counted:
        counted[(x,y)] += 1
    else:
        counted[(x,y)] = 1

def addCoords(first, last, idx):
    diff = first[idx] - last[idx]
    step = 1 if diff < 0 else -1

    for i in range(0, abs(diff) + 1):
        if idx == 0:
            checkThenAddCoord(first[0] + step*i, first[1])
        elif idx == 1:
            checkThenAddCoord(first[0], first[1] + step*i)

def addCoordsD(first, last):
    xDiff = first[0] - last[0]
    yDiff = first[1] - last[1]

    xStep = 1 if xDiff < 0 else -1
    yStep = 1 if yDiff < 0 else -1

    for i in range(0, abs(xDiff) + 1):
        checkThenAddCoord(first[0] + xStep*i, first[1] + yStep*i)
    
    return

def loadAndProcess(mode):
    counted.clear()
    
    with open('../input/day5.txt') as file:
        myList = [line.strip() for line in file]


    for line in myList:
        coords = line.split(' -> ')

        first = map(int, coords[0].split(','))
        last = map(int, coords[1].split(','))

        diag = abs(last[0] - first[0]) - abs(last[1] - first[1]) == 0

        if first[0] == last[0]:
            addCoords(first, last, 1)
        elif first[1] == last[1]:
            addCoords(first, last, 0)
        elif diag and mode == 'part2':
            addCoordsD(first, last)

    moreThanOne = 0
    for item in counted:
        if counted[item] > 1:
            moreThanOne += 1
    
    return moreThanOne

partOne = loadAndProcess('part1')
partTwo = loadAndProcess('part2')

print('partOne = ' + str(partOne))
print('partTwo = ' + str(partTwo))

# $ python3 day4.py
# partOne = 6007
# partTwo = 19349