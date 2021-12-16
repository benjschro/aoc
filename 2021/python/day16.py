from bitstring import BitString

with open('../input/day16.txt') as file:
    fileInput = [line.strip() for line in file]

a = BitString('0x' + fileInput[0])

vVals = []
literals = []
def parsePacket(idx):

    V = int(str(a[idx:idx+3]), 2)
    T = int(str(a[idx+3:idx+6]), 2)

    idx += 6

    groups = []
    if T == 4:
        vVals.append(V)
        numString = None
        while True:
            prefix = a[idx]
            groups.append(a[idx+1:idx+5].bin)
            idx += 5
            if not prefix:
                break
        literal = '0b'
        for n in groups:
            literal += n
        literal = int(literal, 2)
        return idx, literal
    else:
        vVals.append(V)
        I = a[idx]
        idx += 1
        results = []
        if not I:
            L = a[idx:idx+15].int
            idx += 15
            idx_complete = idx + L            
            while idx < idx_complete:
                jdx, literal = parsePacket(idx)
                results.append(literal)
                idx = jdx
        else:
            L = a[idx:idx+11].int
            idx += 11
            while L > 0:
                jdx, literal = parsePacket(idx)
                results.append(literal)
                idx = jdx
                L -= 1

        result = None
        if T == 0:
            result = 0
            for r in results:
                result += r
        elif T == 1:
            result = 1
            for r in results:
                result *= r
        elif T == 2:
            for r in results:
                if result is None or r < result:
                    result = r
        elif T == 3:
            for r in results:
                if result is None or r > result:
                    result = r
        elif T == 5:
            result = 1 if results[0] > results[1] else 0
        elif T == 6:
            result = 1 if results[0] < results[1] else 0
        elif T == 7:
            result = 1 if results[0] == results[1] else 0

        return idx, result

idx, result = parsePacket(0)
print('partOne = ' + str(sum(vVals)))
print('partTwo = ' + str(result))
