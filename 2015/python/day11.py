import collections

with open('../input/day11.txt') as file:
    lines = [line.strip() for line in file]

def getNewPassword(password):
    validPassword = False

    password = list(password)

    while validPassword is False:
        for i in range(len(password) - 1, 0, -1):
            if password[i] != 'z':
                password[i] = chr(ord(password[i]) + 1)
                break
            else:
                password[i] = 'a'

        rule1 = False
        d = collections.deque(maxlen=3)
        for c in password:
            d.append(ord(c))
            if len(d) == 3 and d[0] + 2 == d[1] + 1 == d[2]:
                rule1 = True
                break
        if not rule1:
            continue
        
        rule2 = True
        for c in ['i', 'o', 'l']:
            if c in password:
                rule2 = False
                break
        if not rule2:
            continue
        
        rule3 = False
        pairs = set()
        for i in range(len(password) - 1):
            pair = password[i] + password[i+1]
            if pair[0] == pair[1]:
                pairs.add(pair)
            if len(pairs) >= 2:
                rule3 = True
                break
        if not rule3:
            continue

        break

    newPassword = ''
    for c in password:
        newPassword += c
    
    return newPassword

partOne = getNewPassword(lines[0])
partTwo = getNewPassword(partOne)
print('partOne = ' + str(partOne))
print('partTwo = ' + str(partTwo))
