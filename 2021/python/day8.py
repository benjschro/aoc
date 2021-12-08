with open('../input/day8.txt') as file:
    myList = [line.strip() for line in file]

discoveredSignals = {}

numSegmentCounts = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

def addToDict(items):
    for item in items:
        if len(item) == 2:
            discoveredSignals[1] = item
        elif len(item) == 4:
            discoveredSignals[4] = item
        elif len(item) == 3:
            discoveredSignals[7] = item
        elif len(item) == 7:
            discoveredSignals[8] = item

def solveNumber(numToSolve, refNum, signalPatterns, expectedMatches):
    for signalPattern in signalPatterns:
        if signalPattern in discoveredSignals.values():
            continue
        elif len(signalPattern) == numSegmentCounts[numToSolve]:
            count = 0
            for letter in discoveredSignals[refNum]:
                if letter in signalPattern:
                    count += 1
            if count == expectedMatches:
                return signalPattern

partOneSum = 0
partTwoSum = 0
for line in myList:
    discoveredSignals.clear()

    signalPatterns = line.split('|')[0].strip().split(' ')
    addToDict(signalPatterns)

    segments = line.split('|')[1].strip().split(' ')

    discoveredSignals[2] = solveNumber(numToSolve=2, refNum=4, signalPatterns=signalPatterns, expectedMatches=2) # 1,2,4,7,8 are solved
    discoveredSignals[3] = solveNumber(numToSolve=3, refNum=1, signalPatterns=signalPatterns, expectedMatches=2) # 1,2,3,4,7,8 are solved
    discoveredSignals[5] = solveNumber(numToSolve=5, refNum=1, signalPatterns=signalPatterns, expectedMatches=1) # 1,2,3,4,5,7,8 are solved
    discoveredSignals[6] = solveNumber(numToSolve=6, refNum=7, signalPatterns=signalPatterns, expectedMatches=2) # 1,2,3,4,5,6,7,8 are solved
    discoveredSignals[0] = solveNumber(numToSolve=0, refNum=3, signalPatterns=signalPatterns, expectedMatches=4) # 0,1,2,3,4,5,6,7,8 are solved
    discoveredSignals[9] = solveNumber(numToSolve=9, refNum=3, signalPatterns=signalPatterns, expectedMatches=5) # All digits solved
 
    solvedOutput = ''

    for item in discoveredSignals:
        discoveredSignals[item] = ''.join(sorted(discoveredSignals[item]))

    for i in range(0, len(segments)):
        segments[i] = ''.join(sorted(segments[i]))
    
    for segment in segments:
        for number, letters in discoveredSignals.items():
            if segment == letters:
                solvedOutput += str(number)
                if number in [1,4,7,8]:
                    partOneSum += 1
                break

    partTwoSum += int(solvedOutput)

print('partOne = ' + str(partOneSum))
print('partTwo = ' + str(partTwoSum))

# $ python3 day8.py
# partOne = 445
# partTwo = 1043101
