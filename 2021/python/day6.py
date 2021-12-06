with open('../input/day6.txt') as file:
    myList = [line.strip() for line in file]

fishList = map(int, myList[0].split(','))
fishDictOrig = {}

for fish in fishList:
    if fish not in fishDictOrig:
        fishDictOrig[fish] = 1
    else:
        fishDictOrig[fish] += 1

def simDays(days):
    fishDict = fishDictOrig.copy()
    fishDictTemp = {}
    for i in range(0, days):
        fishDictTemp.clear()
        for j in range(0, 9):
            if j in fishDict:
                if j == 0:
                    fishDictTemp[6] = fishDict[0]
                    fishDictTemp[8] = fishDict[0]
                else:
                    if j == 7:
                        if 6 in fishDictTemp:
                            fishDictTemp[6] += fishDict[7]
                        else:
                            fishDictTemp[6] = fishDict[7]
                    else:
                        fishDictTemp[j-1] = fishDict[j]

        fishDict = fishDictTemp.copy()
    
    sum = 0
    for item in fishDict:
        sum += fishDict[item]
    return sum

print('partOne = ' + str(simDays(80)))
print('partTwo = ' + str(simDays(256)))

# $ python3 day6.py
# partOne = 352151
# partTwo = 1601616884019

