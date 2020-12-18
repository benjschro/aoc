with open('../input/day10.txt') as file:
    lines = [line.strip() for line in file]


def lookAndSay(sequence):
    runLength = 1
    lastNumber = sequence[0]
    newSequence = ''

    for i in range(1, len(sequence)):
        if sequence[i] == lastNumber:
            runLength += 1
        else:
            newSequence += str(runLength)
            newSequence += lastNumber
            runLength = 1
            lastNumber = sequence[i]

    newSequence += str(runLength)
    newSequence += lastNumber

    return newSequence

sequence = lines[0]
for i in range(0, 40):
    sequence = lookAndSay(sequence)

print('partOne = ' + str(len(sequence)))

for i in range(0, 10):
    sequence = lookAndSay(sequence)

print('partTwo = ' + str(len(sequence)))
