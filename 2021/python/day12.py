with open('../input/day12.txt') as file:
    myList = [line.strip() for line in file]

mapDict = {}

for line in myList:
    nodes = line.split('-')
    if nodes[0] in mapDict and nodes[1] != 'start':
        mapDict[nodes[0]].append(nodes[1])
    elif nodes[1] != 'start':
        mapDict[nodes[0]] = [nodes[1]]
    
    nodes = line.split('-')
    if nodes[1] in mapDict and nodes[0] != 'start':
        mapDict[nodes[1]].append(nodes[0])
    elif nodes[0] != 'start':
        mapDict[nodes[1]] = [nodes[0]]

paths = [['start']]

def checkLowerCount(path):
    lowers = {}
    for stop in path:
        if stop.islower():
            if stop in lowers:
                lowers[stop] += 1
            else:
                lowers[stop] = 1
    return max(lowers.values()) < 2

paths = []
def visitNextStop(path, partTwo):
    global paths
    if path[-1] == 'end':
        paths.append(path)
        return
    
    nextStops = mapDict[path[-1]]

    for nextStop in nextStops:

        if nextStop.islower() and nextStop in path and (not checkLowerCount(path) or not partTwo):
            continue
        
        tmp = path.copy()
        tmp.append(nextStop)
        visitNextStop(tmp, partTwo)

    return

visitNextStop(['start'], False)
print('partOne = ' + str(len(paths)))
paths.clear()
visitNextStop(['start'], True)
print('partTwo = ' + str(len(paths)))
