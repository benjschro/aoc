import collections

with open('../input/day9.txt') as file:
    lines = [int(line.strip()) for line in file]

d = collections.deque(maxlen=25)
for i in range(0, 25):
    d.append(lines[i])


for i in range(25, len(lines)):
    nextNum = lines[i]
    match = False
    for j in range(0, 24):
        match = False
        for k in range(1, 25):
            if d[j] + d[k] == nextNum:
                match = True
                break
        if match == True:
            break
    if match == False:
        print('partOne = ' + str(nextNum))
        break
    else:
        d.append(lines[i])

def mySum(start, stop):
    sum = 0
    for i in range(start, stop):
        sum += lines[i]
    
    return sum

rangeLen = 2
idx = 0
match = False
while not match:
    for i in range(0, len(lines) - rangeLen + 1):
        sum = mySum(i, i + rangeLen)
        if sum == 400480901:
            match = True
            idx = i
            break
    rangeLen += 1

mmax = -999999999999999
mmin = 999999999999999

for i in range(idx, idx + rangeLen):
    mmax = max(lines[i], mmax)
    mmin = min(lines[i], mmin)


print('partTwo = ' + str(mmax + mmin))
