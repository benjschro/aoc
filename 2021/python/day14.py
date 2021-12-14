from collections import Counter

with open('../input/day14.txt') as file:
    myList = [line.strip() for line in file]

template = myList[0]
pairs = {}

for i in range(2, len(myList)):
    pair = myList[i].split(' -> ')
    pairs[pair[0]] = pair[1]

newPairs = {}

def step():
    global pairs
    global newPairs
    newPairsUpdate = {}
    for i, pair in enumerate(newPairs):
        mult = newPairs[pair]
        newPairLetter = pairs[pair]
        if pair[0] + newPairLetter not in newPairsUpdate:
            newPairsUpdate[pair[0] + newPairLetter] = mult
        else:
            newPairsUpdate[pair[0] + newPairLetter] += mult
        
        if newPairLetter + pair[1] not in newPairsUpdate:
            newPairsUpdate[newPairLetter + pair[1]] = mult
        else:
            newPairsUpdate[newPairLetter + pair[1]] += mult

    newPairs = newPairsUpdate


def stepCount(x):
    newPairs.clear()

    for i in range(0, len(template) - 1):
        pair = template[i] + template[i+1]
        if pair not in newPairs:
            newPairs[pair] = 1
        else:
            newPairs[pair] += 1

    for i in range(0, x):
        step()

    letterDict = {}
    for pair in newPairs:
        for letter in pair:
            if letter in letterDict:
                letterDict[letter] += newPairs[pair]
            else:
                letterDict[letter] = newPairs[pair]

    finalDict = {}
    for letter in letterDict:
        finalDict[letter] = (letterDict[letter] + 1) // 2


    highest = None
    lowest = None
    for i, val in enumerate(finalDict):
        if highest is None or finalDict[val] > highest:
            highest = finalDict[val]
        if lowest is None or finalDict[val] < lowest:
            lowest = finalDict[val]

    return highest - lowest

print('partOne = ' + str(stepCount(10)))
print('partTwo = ' + str(stepCount(40)))