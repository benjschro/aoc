with open('../input/day16.txt') as file:
    lines = [line.strip() for line in file]

keywords = ['class', 'row', 'seat']

ranges = []

rejectList = []
mode = 0
for line in lines:
    if line.startswith('nearby tickets:'):
        mode = 1
        continue
    if mode == 0:
        for keyword in keywords:
            if line.startswith(keyword):
                tmp = line.split(': ')
                tmp = tmp[1].split(' or ')
                for item in tmp:
                    newRange = item.split('-')
                    ranges.append([int(newRange[0]), int(newRange[1])])
    if mode == 1:
        items = line.split(',')
        for item in items:
            found = False
            for r in ranges:
                if r[0] <= int(item) <= r[1]:
                    found = True
            if not found:
                rejectList.append([int(item) for item in line.split(',')])

# print(rejectList)
# exit()
ranges = {}
myTicket = ''
nearbyTickets = []
mode = 0
for line in lines:
    # if line.startswith('nearby tickets:'):
    #     mode = 1
    #     continue
    if mode == 0:
        if line != '':
            keyword = line.split(': ')[0]
            tmp = line.split(': ')[1]
            tmp = tmp.split(' or ')
            tmpList = []
            for item in tmp:
                newRange = item.split('-')
                if keyword in ranges:
                    ranges[keyword].append([int(newRange[0]), int(newRange[1])])
                else:
                    ranges[keyword] = [[int(newRange[0]), int(newRange[1])]]
        else:
            mode = 1
    elif mode == 1:
        if line.startswith('your ticket:'):
            mode = 2
    elif mode == 2:        
        myTicket = [int(item) for item in line.split(',')]
        mode = 3
    elif mode == 3:
        if line.startswith('nearby tickets:'):
            mode = 4
    elif mode == 4:
        ticket = [int(item) for item in line.split(',')]
        if ticket not in rejectList:
            nearbyTickets.append(ticket)


mapping = {}
for key in ranges:
    idx = 0
    # if key == 'departure location':
        # print(ranges[key])
    while idx < len(nearbyTickets[0]):
        invalid = False
        for abc, ticket in enumerate(nearbyTickets):
            ticketOkay = False
            for r in ranges[key]:
                if r[0] <= ticket[idx] <= r[1]:
                    ticketOkay = True
                    break
            if not ticketOkay:
                # if key == 'departure location':
                    # print(str(idx) + ' (' + str(ticket[idx]) + '): ' + str(ticket))
                invalid = True
                break

        if not invalid:
            if key not in mapping:
                mapping[key] = [idx]
            else:
                mapping[key].append(idx)

        idx += 1
    # exit()

figuredOut = [2, 1, 5, 19, 15, 11, 12, 13, 3, 18, 6, 10, 0, 16, 8, 7, 4, 14, 17, 9]
for m in mapping:
    for f in figuredOut:
        if f in mapping[m]:
            mapping[m].remove(f)
print(mapping)

# price = 1
# class = 2
# duration = 5
# arrival location = 19
# arrival track = 15
# departure station = 11
# departure track = 12
# departure date = 13
# departure location = 3
# departure platform = 18
# departure time = 6
# arrival platform = 10
# zone = 0
# type = 16
# seat = 8
# route = 7
# train = 4
# row = 14
# arrival station = 17
# wagon = 9

nums = [11,12,13,3,18,6]
prod = 1
for num in nums:
    prod *= myTicket[num]
print(prod)

# myProd = 1
# for i in range(0, 6):
#     myProd *= myTicket[i]

# print(myProd)
# print(rejectList)

# sum = 0
# for item in rejectList:
#     sum += item
# print(sum)

# 441254988313 (first 6) is wrong