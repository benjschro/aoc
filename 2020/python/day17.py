with open('../input/day17.txt') as file:
    lines = [line.strip() for line in file]


activeCoords = []
for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        if lines[y][x] == '#':
            activeCoords.append((x, y, 0, 0))


def getNeighbors(coord):
    nearbyList = [-1, 0, 1]

    neighborList = []
    for i in nearbyList:
        for j in nearbyList:
            for k in nearbyList:
                for l in nearbyList:
                    if (i == j == k == l == 0) == False:
                        neighborList.append((coord[0]+i, coord[1]+j, coord[2]+k, coord[3]+l))

    return neighborList


def simulate():
    global activeCoords

    neighborCounts = {}

    for coord in activeCoords:
        counts = 0
        for neighbor in getNeighbors(coord):
            if neighbor in neighborCounts:
                neighborCounts[neighbor] += 1
            else:
                neighborCounts[neighbor] = 1

    updatedActiveCoords = []
    for coord in neighborCounts:
        if coord in activeCoords:
            if 2 <= neighborCounts[coord] <= 3:
                updatedActiveCoords.append(coord)
        else:
            if neighborCounts[coord] == 3:
                updatedActiveCoords.append(coord)

    activeCoords = updatedActiveCoords

for i in range(0, 6):
    simulate()

print(len(activeCoords))
