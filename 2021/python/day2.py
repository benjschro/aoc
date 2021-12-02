with open('../input/day2.txt') as file:
    myList = [line.strip() for line in file]

def partOne():
    pos = 0
    depth = 0

    for line in myList:
        cmd = line.split(' ')[0]
        num = int(line.split(' ')[1])

        if cmd == 'forward':        
            pos += num
        elif cmd == 'down':
            depth += num
        elif cmd == 'up':
            depth -= num
    
    return pos * depth

def partTwo():
    pos = 0
    aim = 0
    depth = 0

    for line in myList:
        cmd = line.split(' ')[0]
        num = int(line.split(' ')[1])

        if cmd == 'forward':        
            pos += num
            depth += (aim * num)
        elif cmd == 'down':
            aim += num
        elif cmd == 'up':
            aim -= num
    
    return pos * depth

print("partOne = " + str(partOne()))
print("partTwo = " + str(partTwo()))

# $ python3 day2.py
# partOne = 1648020
# partTwo = 1759818555