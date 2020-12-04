with open('../input/day3.txt') as file:
    input = file.readline()

coord = [0, 0]
partOneList = []
partOneList.append(coord.copy())

santaCoord = [0, 0]
roboCoord = [0, 0]
partTwoList = []
partTwoList.append(santaCoord.copy())

counter = 0
for direction in input:
    xMod = 0
    yMod = 0

    if direction == '>':
        xMod = 1
    elif direction == '<':
        xMod = -1
    elif direction == '^':
        yMod = 1
    elif direction == 'v':
        yMod = -1
    
    coord[0] += xMod
    coord[1] += yMod

    if counter % 2 == 0:
        santaCoord[0] += xMod
        santaCoord[1] += yMod
    else:
        roboCoord[0] += xMod
        roboCoord[1] += yMod

    if santaCoord not in partTwoList:
        partTwoList.append(santaCoord.copy())

    if roboCoord not in partTwoList:
        partTwoList.append(roboCoord.copy())
    
    if coord not in partOneList:
        partOneList.append(coord.copy())
    
    counter += 1

print('partOne = ' + str(len(partOneList)))
print('partTwo = ' + str(len(partTwoList)))

# $ python3 day3.py
# partOne = 2081
# partTwo = 2341