import math

with open('../input/day16.txt') as file:
    fileInput = [line.strip() for line in file]

a = format(int(fileInput[0], 16), str(len(fileInput[0])*2) + 'b')

VList = []
def parsePacket(idx):
    V = int(a[idx:idx+3], 2)
    VList.append(V)
    T = int(a[idx+3:idx+6], 2)

    idx += 6

    if T == 4:
        groups = ''
        while True:
            prefix = a[idx]
            groups += a[idx+1:idx+5]
            idx += 5
            if prefix == '0':
                break
        result = int(groups, 2)
    else:
        I = a[idx]
        results = []
        if I == '0':
            L = int(a[idx+1:idx+16], 2)
            idx += 16
            idx_complete = idx + L            
            while idx != idx_complete:
                idx, literal = parsePacket(idx)
                results.append(literal)
        else:
            L = int(a[idx+1:idx+12], 2)
            idx += 12
            while L > 0:
                idx, literal = parsePacket(idx)
                results.append(literal)
                L -= 1

        if T == 0:
            result = sum(results)
        elif T == 1:
            result = math.prod(results)
        elif T == 2:
            result = min(results)
        elif T == 3:
            result = max(results)
        elif T == 5:
            result = int(results[0] > results[1])
        elif T == 6:
            result = int(results[0] < results[1])
        elif T == 7:
            result = int(results[0] == results[1])

    return idx, result

_, result = parsePacket(0)
print('partOne = ' + str(sum(VList)))
print('partTwo = ' + str(result))
