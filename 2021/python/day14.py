from collections import Counter

with open('../input/day14.txt') as file:
    fileInput = [line.strip() for line in file]

polymer = {}
pairInsertionRules = {}

for i in range(2, len(fileInput)):
    tmp = fileInput[i].split(' -> ')
    pairInsertionRules[tmp[0]] = tmp[1]

for i in range(0, len(fileInput[0]) - 1):
    pair = fileInput[0][i:i+2]
    polymer[pair] = 1 if pair not in polymer else polymer[pair] + 1

def step():
    newPolymer = {}
    for pair in polymer:
        element = pairInsertionRules[pair]
        count = polymer[pair]

        newPair = pair[0] + element
        newPolymer[newPair] = count if newPair not in newPolymer else newPolymer[newPair] + count
        newPair = element + pair[1]
        newPolymer[newPair] = count if newPair not in newPolymer else newPolymer[newPair] + count
    return newPolymer

def solve():
    elementCount = {}
    for pair in polymer:
        count = polymer[pair]
        for element in pair:
            elementCount[element] = count if element not in elementCount else elementCount[element] + count
    
    for element in elementCount:
        elementCount[element] = (elementCount[element] + 1) // 2

    return max(elementCount.values()) - min(elementCount.values())

for _ in range(10):
    polymer = step()
partOne = solve()
for _ in range(30):
    polymer = step()
partTwo = solve()

print('partOne = ' + str(partOne))
print('partTwo = ' + str(partTwo))