with open('../input/day17.txt') as file:
    fileInput = [line.strip() for line in file]

a = fileInput[0].split(': ')
b = a[1].split(', ')

x = b[0].split('=')[1].split('..')
xx = list(map(int, x))
y = b[1].split('=')[1].split('..')
yy = list(map(int, y))

def checkIfInside(coord):
    insideX = (xx[0] <= coord[0]) and (coord[0] <= xx[1])
    insideY = (yy[0] <= coord[1]) and (coord[1] <= yy[1])
    return (insideX and insideY)

def checkIfBeyond(coord):
    tooFarX = coord[0] > xx[1]
    tooShortX = coord[0] < xx[0]
    tooFarY = coord[1] > yy[1]
    tooShortY = coord[1] < yy[0]

    return (tooShortY) or (tooFarX)

maxY = 0

successList = []

def simulate(x, y):
    global maxY
    coord = [0, 0]
    vel = [x, y]

    maxYTemp = 0
    success = False
    while True:
        coord[0] += vel[0]
        coord[1] += vel[1]

        if coord[1] > maxYTemp:
            maxYTemp = coord[1]

        if checkIfInside(coord):
            if maxYTemp > maxY:
                maxY = maxYTemp
            success = True
            successList.append([x, y])
            break
    
        if checkIfBeyond(coord):
            break

        vel[0] = max(vel[0] - 1, 0)
        vel[1] -= 1
        

    return success

for x in range(1, xx[1] + 1):
    for y in range(yy[0], (yy[0] * -2) + 1):
        simulate(x,y)

print('partOne = ' + str(maxY))
print('partTwo = ' + str(len(successList)))