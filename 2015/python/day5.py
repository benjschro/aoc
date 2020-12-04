with open('../input/day5.txt') as file:
    stringList = [line.strip() for line in file]

partOneStringCount = 0
partTwoStringCount = 0
for string in stringList:
    vowelCount = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        for letter in string:
            if letter == vowel:
                vowelCount += 1
    
    doubleLetter = False
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            doubleLetter = True
            break
    
    badStringPresent = False
    for badString in ['ab', 'cd', 'pq', 'xy']:
        if badString in string:
            badStringPresent = True
    
    twoPair = False
    for i in range(0, len(string)-3):
        pair = string[i] + string[i+1]
        if pair in string[i+2:]:
            twoPair = True
            break

    repeatWithSingleSkip = False
    for i in range(0, len(string)-2):
        if string[i] == string[i+2]:
            repeatWithSingleSkip = True
            break

    if vowelCount >= 3 and doubleLetter and not badStringPresent:
        partOneStringCount += 1

    if twoPair and repeatWithSingleSkip:
        partTwoStringCount += 1

print('partOne = ' + str(partOneStringCount))
print('partTwo = ' + str(partTwoStringCount))

# $ python3 day5.py
# partOne = 236
# partTwo = 51