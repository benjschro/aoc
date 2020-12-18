with open('../input/day11.txt') as file:
    lines = [line.strip() for line in file]

currentPassword = list('hepxcrrq')#list(lines[0])
# print(currentPassword)
# exit()

allRulesMet = False
while not allRulesMet:
    for i in range(len(currentPassword) - 1, -1, -1):
        ordChar = ord(currentPassword[i])
        if ordChar < 122:
            ordChar += 1
        else:
            ordChar = 97
        
        if ordChar in [105, 111, 108]:
            ordChar += 1
        
        chrChar = chr(ordChar)
        currentPassword[i] = chrChar

        if ordChar != 97:
            break
    
    # check rule 1
    lastChar = ord(currentPassword[0])
    runLength = 1
    for i in range(1, len(currentPassword)):
        if ord(currentPassword[i]) == lastChar + 1:
            lastChar = ord(currentPassword[i])
            runLength += 1
    if runLength < 3:
        continue
    
    # check rule 2
    # for i in range(0, len(currentPassword)):
    #     if currentPassword[i] in ['i', 'o', 'l']:
    #         allRulesMet = False
    #         break
    
    pairCount = 0
    i = 0
    while i < len(currentPassword) - 1:
        if currentPassword[i] == currentPassword[i+1]:
            pairCount += 1
            i += 2
        else:
            i += 1

    if pairCount < 2:
        continue
    
    allRulesMet = True

print(''.join(currentPassword))

# hxbyiijj is wrong