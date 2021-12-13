with open('../input/day13.txt') as file:
    myList = [line.strip() for line in file]


def foldHorizontal(y):
    global coordList
    tmp = set()
    for i, coord in enumerate(coordList):
        if coord[1] >= y:
            tmp.add((coord[0], y - (coord[1] - y)))
        else:
            tmp.add(coord)

    return tmp

def foldVertical(x):
    global coordList
    tmp = set()
    for i, coord in enumerate(coordList):
        if coord[0] >= x:
            tmp.add((x - (coord[0] - x), coord[1]))
        else:
            tmp.add(coord)

    return tmp

partOne = None
coordList = set()
for line in myList:
    if line == '':
        continue
    elif line.split(' ')[0] == 'fold':
        foldRule = line.split(' ')[2]
        foldDirection = foldRule.split('=')[0]
        foldValue = int(foldRule.split('=')[1])
        if foldDirection == 'y':
            coordList = foldHorizontal(foldValue)
        else:
            coordList = foldVertical(foldValue)
        if partOne == None:
            partOne = len(coordList)
    else:
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        coordList.add((x,y))

print('partOne = ' + str(partOne))
print('partTwo = ')

for y in range(0, 7):
    rowStr = ''
    for x in range(0, 100):
        if (x, y) in coordList:
            rowStr += '#'
        else:
            rowStr += ' '
    print(rowStr)