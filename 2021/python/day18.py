import re

with open('../input/day18.txt') as file:
    fileInput = [line.strip() for line in file]

def explode(sum):
    depth = -1
    for i, c in enumerate(sum):
        depth += 1 if c == '[' else -1 if c == ']' else 0

        if depth == 4:
            r = re.findall('[0-9]+,[0-9]+', sum[i:])
            bias = len(r[0]) + 2
            lAdd = int(r[0].split(',')[0])
            rAdd = int(r[0].split(',')[1])

            # add the number to the left
            r = list(map(int, re.findall('[0-9]+', sum[:i])))
            tmpString = re.sub('[0-9]+', '.', sum[:i])
            if len(r) > 0:
                r[-1] += lAdd
            
            lString = ''            
            j = 0
            for c in tmpString:
                if c != '.':
                    lString += c
                else:
                    lString += str(r[j])
                    j += 1

            # add the number to the right
            r = list(map(int, re.findall('[0-9]+', sum[i+bias:])))
            tmpString = re.sub('[0-9]+', '.', sum[i+bias:])
            if len(r) > 0:
                r[0] += rAdd
            
            rString = ''
            j = 0
            for c in tmpString:
                if c != '.':
                    rString += c
                else:
                    rString += str(r[j])
                    j += 1
            
            return lString + '0' + rString
    return sum


def split(sum):
    r = list(map(int, re.findall('[0-9]+', sum)))
    tmpString = re.sub('[0-9]+', '.', sum)

    newString = ''
    j = 0
    splitComplete = False
    for c in tmpString:
        if c != '.':
            newString += c
        else:
            if r[j] < 10 or splitComplete:
                newString += str(r[j])
            else:
                div = r[j] // 2
                mod = r[j] % 2
                newString += '[' + str(div) + ',' + str(div+mod) + ']'      
                splitComplete = True      
            j += 1
    return newString

def explodeLoop(sum):
    initSum = sum
    while True:        
        newSum = explode(initSum)
        if newSum == initSum:
            return newSum
        else:
            initSum = newSum

def reduceLoop(sum):
    initSum = sum
    while True:
        newSum = explodeLoop(initSum)
        newSum = split(newSum)
        if newSum == initSum:
            return newSum
        else:
            initSum = newSum

def addInputs():
    global fileInput
    sum = None
    for line in fileInput:
        if sum is None:
            sum = line
        else:
            sum = '[' + sum + ',' + line + ']'
            sum = reduceLoop(sum)
    return sum

def getMagnitude(sum):
    magnitude = []
    while True:
        r = re.findall('[0-9]+,[0-9]+', sum)
        if len(r) < 1:
            break
        tmpString = re.sub('\[[0-9]+,[0-9]+\]', '.', sum)

        magnitude.clear()
        for pair in r:
            p = list(map(int, pair.split(',')))
            newMag = (p[0]*3) + (p[1]*2)
            magnitude.append(newMag)

        j = 0
        sum = ''
        for c in tmpString:
            if c != '.':
                sum += c
            else:
                sum += str(magnitude[j])
                j += 1
    return sum

sum = addInputs()
sum = getMagnitude(sum)
print('partOne = ' + str(sum))

mag = 0
for i in range(0, len(fileInput) - 2):
    for j in range(i+1, len(fileInput) - 1):
        p1 = fileInput[i]
        p2 = fileInput[j]

        sum = '[' + p1 + ',' + p2 + ']'
        sum = reduceLoop(sum)
        mag2 = int(getMagnitude(sum))
        if mag2 > mag:
            mag = mag2
        
        sum = '[' + p2 + ',' + p1 + ']'
        sum = reduceLoop(sum)
        mag2 = int(getMagnitude(sum))
        if mag2 > mag:
            mag = mag2

print('partTwo = ' + str(mag))

