with open('../input/day13.txt') as file:
    lines = [line.strip() for line in file]

earliest = int(lines[0])
data = lines[1].split(',')

busDeltas = {}

for bus in data:
    if bus.isnumeric():
        mySum = 0
        while mySum <= earliest:
            mySum += int(bus)
        # print(mySum)
        busDeltas[bus] = mySum - earliest

key = min(busDeltas, key=busDeltas.get)
partOne = int(key) * busDeltas[key]
print(partOne)


# data = '7,13,x,x,59,x,31,19'.split(',')
# data = '17,x,13,19'.split(',')
# data = '1789,37,47,1889'.split(',')

buses = []
offsets = []
inc = 0

for i, bus in enumerate(data):
    if bus.isnumeric():
        buses.append(int(bus))
        offsets.append(i)
        if inc == 0:
            inc = int(bus)


foundList = [buses[0]]
done = False
inc = buses[0]

target = 0
while not done:
    target += inc
    for i in range(1, len(buses)):
        if (target + offsets[i]) % buses[i] == 0:
            if buses[i] not in foundList:
                foundList.append(buses[i])
                inc *= buses[i]
                if len(foundList) == len(buses):
                    done = True

print(target)












