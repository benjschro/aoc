with open('../input/day1.txt') as file:
    myList = [int(line.strip()) for line in file]

partOne = 0
partTwo = 0
for i in range(0, len(myList)):
    if partOne == 0 or partTwo == 0:
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == 2020:
                partOne = myList[i] * myList[j]
            if partTwo == 0:
                for k in range(i+2, len(myList)):
                    if myList[i] + myList[j] + myList[k] == 2020:
                        partTwo = myList[i] * myList[j] * myList[k]
                        break
    else:
        break

print("partOne = " + str(partOne))
print("partTwo = " + str(partTwo))

# $ python3 day1.py
# partOne = 1003971
# partTwo = 84035952