with open('../input/day12.txt') as file:
    lines = [line.strip() for line in file]

facing = 'E'
x = 0
y = 0

def rotateRight(num):
    global facing
    tempNum = num
    while tempNum > 0:
        if facing == 'E':
            facing = 'S'
        elif facing == 'S':
            facing = 'W'
        elif facing == 'W':
            facing = 'N'
        elif facing == 'N':
            facing = 'E'
        else:
            print('error')
            exit()
        tempNum -= 90

def rotateLeft(num):
    global facing
    tempNum = num
    while tempNum > 0:
        if facing == 'E':
            facing = 'N'
        elif facing == 'N':
            facing = 'W'
        elif facing == 'W':
            facing = 'S'
        elif facing == 'S':
            facing = 'E'
        else:
            print('error')
            exit()
        tempNum -= 90

for line in lines:
    direction = line[0]
    extra = int(line[1:])

    if direction == 'R':
        rotateRight(extra)
    elif direction == 'L':
        rotateLeft(extra)
    elif direction == 'F':
        if facing == 'E':
            x += extra
        elif facing == 'N':
            y += extra
        elif facing == 'W':
            x -= extra
        elif facing == 'S':
            y -= extra
    elif direction == 'N':
        y += extra
    elif direction == 'S':
        y -= extra
    elif direction == 'E':
        x += extra
    elif direction == 'W':
        x -= extra
    else:
        print('error')
        exit()

print(abs(x) + abs(y))