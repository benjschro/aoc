with open('../input/day8.txt') as file:
    myList = [line.strip() for line in file]

digitDict = {}

def addToDict(items):
    for item in items:
        if len(item) == 2:
            digitDict[1] = item
        elif len(item) == 4:
            digitDict[4] = item
        elif len(item) == 3:
            digitDict[7] = item
        elif len(item) == 7:
            digitDict[8] = item

partOneSum = 0
partTwoSum = 0
for line in myList:
    digitDict.clear()
    wires = line.split('|')[0].strip().split(' ')
    addToDict(wires)
    segments = line.split('|')[1].strip().split(' ')
    addToDict(segments)

    letterCount = {}
    for letter in 'abcdefg':
        for wire in wires:
            if letter in wire:
                if letter in letterCount:
                    letterCount[letter] += 1
                else:
                    letterCount[letter] = 1
    
    # 1, 4, 7, 8 are solved
    # Solve for 2
    for wire in wires:
        if len(wire) == 5: # 2, 3, 5
            count = 0
            for letter in digitDict[4]:
                if letter in wire:
                    count += 1
            if count == 2:
                digitDict[2] = wire

    # 1, 2, 4, 7, 8 are solved
    # Solve for 3 and 5
    for wire in wires:
        if len(wire) == 5 and digitDict[2] != wire: # 3, 5
            count = 0
            for letter in digitDict[1]:
                if letter in wire:
                    count += 1
            if count == 2:
                digitDict[3] = wire
            elif count == 1:
                digitDict[5] = wire

    # 1, 2, 3, 4, 5, 7, 8 are solved
    # Solve for 6
    for wire in wires:
        if len(wire) == 6: # 0, 6, 9
            count = 0
            for letter in digitDict[7]:
                if letter in wire:
                    count += 1
            if count == 2:
                digitDict[6] = wire

    # 1, 2, 3, 4, 5, 6, 7, 8 are solved
    # Solve for 0 and 9
    for wire in wires:
        if len(wire) == 6 and digitDict[6] != wire: # 0, 9
            count = 0
            for letter in digitDict[3]:
                if letter in wire:
                    count += 1
            if count == 5:
                digitDict[9] = wire
            elif count == 4:
                digitDict[0] = wire

    outputValue = ''

    for item in digitDict:
        digitDict[item] = ''.join(sorted(digitDict[item]))

    for i in range(0, len(segments)):
        segments[i] = ''.join(sorted(segments[i]))
    
    for segment in segments:
        for number, letters in digitDict.items():
            if segment == letters:
                outputValue += str(number)
                if str(number) in '1478':
                    partOneSum += 1
                break

    partTwoSum += int(outputValue)

print('partOne = ' + str(partOneSum))
print('partTwo = ' + str(partTwoSum))

# $ python3 day8.py
# partOne = 445
# partTwo = 1043101
