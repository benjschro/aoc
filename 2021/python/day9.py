with open('../input/day9.txt') as file:
    myList = [line.strip() for line in file]

def getNeighbors(i, j):
    neighborList = []

    # check if neighbor above
    if i != 0:
        neighborList.append(myList[i-1][j])
    
    # check if neighbor below
    if i != len(myList) - 1:
        neighborList.append(myList[i+1][j])
    
    # check if neighbor left
    if j != 0: 
        neighborList.append(myList[i][j-1])

    # check if neighbor right
    if j != len(myList[0]) - 1:
        neighborList.append(myList[i][j+1])
    
    return neighborList

coordList = []

def getHigherCoords(i, j):
    coordListTemp = []
    # check if neighbor above
    if i != 0:
        height = myList[i-1][j]
        if height > myList[i][j] and height != '9':
            coordListTemp.append([i-1, j])
    
    # check if neighbor below
    if i != len(myList) - 1:
        height = myList[i+1][j]
        if height > myList[i][j] and height != '9':
            coordListTemp.append([i+1, j])
    
    # check if neighbor left
    if j != 0: 
        height = myList[i][j-1]
        if height > myList[i][j] and height != '9':
            coordListTemp.append([i, j-1])

    # check if neighbor right
    if j != len(myList[0]) - 1:
        height = myList[i][j+1]
        if height > myList[i][j] and height != '9':
            coordListTemp.append([i, j+1])
    
    return coordListTemp

def getBasinSize(i, j):
    global coordList
    coordList.append([i, j])

    while True:
        coordSize = len(coordList)
        for coord in coordList:
            coordListTemp = getHigherCoords(coord[0], coord[1])
            for c in coordListTemp:
                if c not in coordList:
                    coordList.append(c)
        if len(coordList) == coordSize:
            break

    return len(coordList)


basins = []

lowPoints = []
for i in range(0, len(myList)):
    for j in range(0, len(myList[i])):
        neighbors = getNeighbors(i, j)
        isSmallest = True
        for neighbor in neighbors:
            if myList[i][j] >= neighbor:
                isSmallest = False
                break
        if isSmallest is True:
            coordList.clear()
            basinSize = getBasinSize(i, j)
            basins.append(basinSize)
            lowPoints.append(myList[i][j])

sum = 0
for point in lowPoints:
    sum += int(point) + 1

print('partOne = ' + str(sum))
basins = sorted(basins, reverse=True)

print('partTwo = ' + str(basins[0] * basins[1] * basins[2]))

# $ python3 day9.py
# partOne = 570
# partTwo = 899392