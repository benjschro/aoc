import heapq

with open('../input/day15.txt') as file:
    fileInput = [line.strip() for line in file]

def c2s(c):
    return str(c[0]) + ',' + str(c[1])

graph = {}

def createGraph():
    global graph
    graph.clear()
    for y in range(len(fileInput)):
        for x in range(len(fileInput[y])):
            c = [x,y]
            neighbors = getNeighbors(c)
            graph[c2s(c)] = {}
            for n in neighbors:
                graph[c2s(c)][c2s(n)] = int(fileInput[n[0]][n[1]])

def expandFile():
    global fileInput
    newFile = []
    for loop1 in range(1):
        for line in fileInput:
            newLine = ''
            for loop2 in range(5):
                for c in line:
                    cc = int(c) + loop2
                    cc = cc - 9 if cc > 9 else cc
                    newLine += str(cc)
            newFile.append(newLine)
    fileInput = newFile

    newFile = []
    for loop1 in range(5):
        for line in fileInput:
            newLine = ''
            for c in line:
                cc = int(c) + loop1
                cc = cc - 9 if cc > 9 else cc
                newLine += str(cc)
            newFile.append(newLine)
    fileInput = newFile

def getNeighbors(coord):
    neighborList = []

    i, j = coord[0], coord[1]

    # check if neighbor above
    if i != 0 and [i-1,j] not in neighborList:
        neighborList.append([i-1,j])
    
    # check if neighbor below
    if i != len(fileInput) - 1 and [i+1,j] not in neighborList:
        neighborList.append([i+1,j])
    
    # check if neighbor left
    if j != 0 and [i,j-1] not in neighborList:
        neighborList.append([i,j-1])

    # check if neighbor right
    if j != len(fileInput[0]) - 1 and [i,j+1] not in neighborList:
        neighborList.append([i,j+1])

    return neighborList

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

createGraph()
S = calculate_distances(graph, c2s([0, 0]))
print('partOne = ' + str(S[c2s([99,99])]))

expandFile()
createGraph()
S = calculate_distances(graph, c2s([0, 0]))
print('partTwo = ' + str(S[c2s([499,499])]))
