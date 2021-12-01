with open('../input/day1.txt') as file:
    myList = [int(line.strip()) for line in file]

last1 = None
last2 = None
last3 = None
lastSum = None

partOne = 0
partTwo = 0

for item in myList:
    if last1 is None:
        last1 = item
    elif last2 is None:
        last2 = item
    elif last3 is None:
        last3 = item
        lastSum = last1 + last2 + last3
    else:
        last1 = last2
        last2 = last3
        last3 = item
        newSum = last1 + last2 + last3
        if newSum > lastSum:
            partTwo += 1
        lastSum = newSum
    
    if last2 is not None:
        if last2 > last1:
            partOne += 1

print("partOne = " + str(partOne))
print("partTwo = " + str(partTwo))

# $ python3 day1.py
# partOne = 1316
# partTwo = 1344