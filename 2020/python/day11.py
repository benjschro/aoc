import copy

with open('../input/day11.txt') as file:
    lines = [line.strip() for line in file]

coords = {}
coordsCopy = {}

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        coords[(x, y)] = lines[y][x]


def countOccupiedAdjacent(x, y):
    spotsToCheck = []
    if x > 0:
        spotsToCheck.append((x-1, y))

    if x < len(lines[0]) - 1:
        spotsToCheck.append((x+1, y))
        
    if y > 0:
        spotsToCheck.append((x, y-1))

        if x < len(lines[0]) - 1:
            spotsToCheck.append((x+1, y-1))
        if x > 0:
            spotsToCheck.append((x-1, y-1))

    if y < len(lines) - 1:
        spotsToCheck.append((x, y+1))

        if x < len(lines[0]) - 1:
            spotsToCheck.append((x+1, y+1))
        if x > 0:
            spotsToCheck.append((x-1, y+1))
    
    count = 0
    for coord in spotsToCheck:
        if coords[coord] == '#':
            count += 1
    return count

def countDirection(x, y, xMod, yMod):
    xModL = xMod
    yModL = yMod
    while 0 <= x + xModL < len(lines[0]) and 0 <= y + yModL < len(lines):
        if coords[(x+xModL, y+yModL)] == '#':
            return 1
        elif coords[(x+xModL, y+yModL)] == 'L':
            return 0
        else:
            yModL = yModL + yMod
            xModL = xModL + xMod
    return 0

def countOccupiedInSight(x, y):
    count = 0
    count += countDirection(x, y, -1, 0)
    count += countDirection(x, y, 1, 0)
    count += countDirection(x, y, 0, -1)
    count += countDirection(x, y, 0, 1)
    count += countDirection(x, y, -1, -1)
    count += countDirection(x, y, 1, 1)
    count += countDirection(x, y, 1, -1)
    count += countDirection(x, y, -1, 1)
    return count


def countTotalOccupied():
    count = 0
    for item in coords:
        if coords[item] == '#':
            count += 1
    return count

def iterate():
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if coordsCopy[(x, y)] == 'L':
                if countOccupiedAdjacent(x, y) == 0:
                    coordsCopy[(x, y)] = '#'
            elif coordsCopy[(x, y)] == '#':
                if countOccupiedAdjacent(x, y) >= 4:
                    coordsCopy[(x, y)] = 'L'

def iterateTwo():
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if coordsCopy[(x, y)] == 'L':
                if countOccupiedInSight(x, y) == 0:
                    coordsCopy[(x, y)] = '#'
            elif coordsCopy[(x, y)] == '#':
                if countOccupiedInSight(x, y) >= 5:
                    coordsCopy[(x, y)] = 'L'






# lastCount = 0
# sameCount = 0
# iterations = 0
# while sameCount != 10:
#     coordsCopy = coords.copy()
#     iterate()
#     coords = coordsCopy.copy()

#     tempCount = countTotalOccupied()
#     if tempCount == lastCount:
#         sameCount += 1
#     else:
#         lastCount = tempCount
#     iterations += 1

lastCount = 0
sameCount = 0
iterations = 0
while sameCount != 10:
    coordsCopy = coords.copy()
    iterateTwo()
    coords = coordsCopy.copy()

    tempCount = countTotalOccupied()
    if tempCount == lastCount:
        sameCount += 1
    else:
        sameCount = 0

    lastCount = tempCount
    iterations += 1

print(tempCount)
