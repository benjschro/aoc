file = open('../input/day1.txt', 'r')
directions = file.read()
file.close()

directions = directions.replace(' ', '').split(',')

X = 0
Y = 0

face = 'N'

def changeFace(d):
    global face
    if face is 'N':
        face = 'W' if d[0] is 'L' else 'E'
    elif face is 'E':
        face = 'N' if d[0] is 'L' else 'S'
    elif face is 'W':
        face = 'S' if d[0] is 'L' else 'N'
    else:
        face = 'E' if d[0] is 'L' else 'W'

def moveFace(d):
    global face
    global X, Y
    if face is 'N':
        Y += 1
    elif face is 'E':
        X += 1
    elif face is 'W':
        X -= 1
    else:
        Y -= 1

coordList = []

partTwo = None
for d in directions:
    changeFace(d)
    for i in range(int(d[1:])):
        moveFace(d)
        if partTwo is None:
            if (X,Y) not in coordList:
                coordList.append((X,Y))
            else:
                partTwo = abs(X) + abs(Y)

print('partOne = ' + str(abs(X) + abs(Y)))
print('partTwo = ' + str(partTwo))

# $ python3 day1.py
# partOne = 230
# partTwo = 154