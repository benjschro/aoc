with open('../input/day15.txt') as file:
    lines = [line.strip() for line in file]

numbers = lines[0].split(',')

def getLastNumberSpoken(rounds):
    myDict = {}
    for i in range(0, len(numbers)):
        myDict[int(numbers[i])] = [i + 1]
        lastNum = int(numbers[i])

    turns = len(numbers) + 1
    while turns < rounds + 1:        
        if len(myDict[lastNum]) == 1:
            nextNum = 0
        else:
            nextNum = myDict[lastNum][1] - myDict[lastNum][0]
        
        if nextNum not in myDict:
            myDict[nextNum] = [turns]
        else:
            if len(myDict[nextNum]) > 1:
                myDict[nextNum].pop(0)
            myDict[nextNum].append(turns)
        
        lastNum = nextNum
        turns += 1
    return lastNum

print(getLastNumberSpoken(2020))
print(getLastNumberSpoken(30000000))
