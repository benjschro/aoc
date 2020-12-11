with open('../input/day7.txt') as file:
    lines = [line.strip() for line in file]

bags = {}
bagsCount = {}
for line in lines:
    words = line.split()
    bag = (words[0], words[1])

    if words[4] == 'no':
        bags[bag] = ('no', 'bag')
        bagsCount[bag] = [0]
    else:
        bags[bag] = []
        bagsCount[bag] = []
        for i in range(4, len(words), 4):
            bags[bag].append((words[i+1], words[i+2]))
            bagsCount[bag].append(int(words[i]))

myBag = ('shiny', 'gold')
count = 0

loopBagList = []

for bag in bags:
    if myBag in bags[bag]:
        if bags[bag] not in loopBagList:
            loopBagList.append(bag)

# count = len(loopBagList)
# countLast = -1

def recurseLook(inBag):
    if myBag in inBag:
        return True
    else:
        for tempBag in inBag:
            if tempBag != 'no' and tempBag != 'bag':
                if recurseLook(bags[tempBag]) == True:
                    return True
    return False


for bag in bags:
    if bag not in loopBagList:
        if recurseLook(bags[bag]) == True:
            loopBagList.append(bag)

print('partOne = ' + str(len(loopBagList))) #378


def partTwoRecurse(inBag):
    count = 1
    if inBag == 'no' or inBag == 'bag':
        return 1

    mult = bagsCount[inBag]

    for i in range(0, len(mult)):
        subBag = bags[inBag][i]
        count += mult[i] * partTwoRecurse(subBag)
    return count


count = partTwoRecurse(myBag)
count -= 1

print('partTwo = ' + str(count))


# $ python3 day7.py
# partOne = 378
# partTwo = 27526