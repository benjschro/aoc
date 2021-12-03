with open('../input/day3.txt') as file:
    myList = [line.strip() for line in file]

def countBits(bit, inputList):
    ones = 0
    zeros = 0

    for line in inputList:
        if line[bit] == '1':
            ones += 1
        else:
            zeros +=1
    
    return ones, zeros

def partOne():
    gamma = ''
    for i in range(12):
        ones, zeros = countBits(i, myList)
        if ones > zeros:
            gamma += '1'
        else:
            gamma += '0'
    
    gamma = int(gamma, 2)

    return gamma * (gamma ^ 0xFFF)

def reduceList(bit, inputList, o2Rules):
    newList = []

    ones, zeros = countBits(bit, inputList)

    for line in inputList:
        if o2Rules:
            if ones > zeros and line[bit] == '1':
                newList.append(line)
            elif zeros > ones and line[bit] == '0':
                newList.append(line)
            elif zeros == ones and line[bit] == '1':
                newList.append(line)
        else:
            if zeros < ones and line[bit] == '0':
                newList.append(line)
            elif ones < zeros and line[bit] == '1':
                newList.append(line)
            elif zeros == ones and line[bit] == '0':
                newList.append(line)

    return newList

def partTwo():
    o2List = myList
    for i in range(12):
        o2List = reduceList(i, o2List, True)
        if len(o2List) == 1:
            break

    co2List = myList
    for i in range(12):
        co2List = reduceList(i, co2List, False)
        if len(co2List) == 1:
            break

    o2 = int(o2List[0], 2)
    co2 = int(co2List[0], 2)

    return o2 * co2

print("partOne = " + str(partOne()))
print("partTwo = " + str(partTwo()))

# $ python3 day3.py
# partOne = 4138664
# partTwo = 4273224