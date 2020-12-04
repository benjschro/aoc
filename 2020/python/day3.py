with open('day3.txt') as file:
    myList = [line.strip() for line in file]

xLen = len(myList[0])
yLen = len(myList)

xPos = [0, 0, 0, 0, 0]
yPos = [0, 0, 0, 0, 0]

xInc = [1, 3, 5, 7, 1]
yInc = [1, 1, 1, 1, 2]

treeCount = [0, 0, 0, 0, 0]
treeProduct = 1
exitVoteCount = 0
while exitVoteCount < 5:
    for i in range(5):
        if yPos[i] < yLen:
            xPos[i] = xPos[i] + xInc[i]
            if xPos[i] >= xLen:
                xPos[i] = xPos[i] - xLen
            yPos[i] = yPos[i] + yInc[i]

            if yPos[i] < yLen:
                if myList[yPos[i]][xPos[i]] == '#':
                    treeCount[i] = treeCount[i] + 1
            else:
                exitVoteCount = exitVoteCount + 1
                treeProduct = treeProduct * treeCount[i]

print('partOne = ' + str(treeCount[1]))
print('partTwo = ' + str(treeProduct))

# $ python3 day3.py
# partOne = 262
# partTwo = 2698900776