with open('../input/day11.txt') as file:
    myList = [line.strip() for line in file]

def getNeighbors(i, j):
    neighborList = []

    # check if neighbor above
    if i != 0:
        neighborList.append([i-1,j])
        #  check if neighbor left
        if j != 0:
            neighborList.append([i-1,j-1])
        # check if neighbor right
        if j != len(myList[0]) - 1:
            neighborList.append([i-1,j+1])

    
    # check if neighbor below
    if i != len(myList) - 1:
        neighborList.append([i+1,j])
        #  check if neighbor left
        if j != 0:
            neighborList.append([i+1,j-1])
        # check if neighbor right
        if j != len(myList[0]) - 1:
            neighborList.append([i+1,j+1])
    
    # check if neighbor left
    if j != 0: 
        neighborList.append([i,j-1])
        # check if neighbor above
        if i != 0:
            neighborList.append([i-1,j-1])
        # check if neighbor below
        if i != len(myList) - 1:
            neighborList.append([i+1,j-1])

    # check if neighbor right
    if j != len(myList[0]) - 1:
        neighborList.append([i,j+1])
        # check if neighbor above
        if i != 0:
            neighborList.append([i-1,j+1])
        # check if neighbor below
        if i != len(myList) - 1:
            neighborList.append([i+1,j+1])

    res = []
    for i in neighborList:
        if i not in res:
            res.append(i)

    return res

newList = []
for i in range(0, len(myList)):
    newRow = []
    for j in range(0, len(myList[0])):
        newRow.append(int(myList[i][j]))
    newList.append(newRow)

flashCount = 0
flashStep = 0
def step():
    global flashCount
    global flashStep
    flashStep = 0
    flashList = []

    for i in range(0, len(newList)):
        for j in range(0, len(newList[0])):
            val = newList[i][j]
            newList[i][j] = val + 1

    while True:
        changesMade = False
        for i in range(0, len(newList)):
            for j in range(0, len(newList[0])):
                val = newList[i][j]
                if val > 9 and [i, j] not in flashList:
                    changesMade = True
                    flashList.append([i, j])
                    neighbors = getNeighbors(i, j)
                    for neighbor in neighbors:
                        newList[neighbor[0]][neighbor[1]] += 1
        if not changesMade:
            break

    for coord in flashList:
        flashCount += 1
        flashStep += 1
        newList[coord[0]][coord[1]] = 0

for i in range(0, 100):
    step()

partOne = flashCount
stepCount = 0
while True:
    step()
    stepCount += 1
    if flashStep == 100:
        break

print('partOne = ' + str(partOne))
print('partTwo = ' + str(stepCount))

# $ python3 day11.py
# partOne = 1725
# partTwo = 208