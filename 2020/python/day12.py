with open('../input/day12.txt') as file:
    lines = [line.strip() for line in file]

x = y = 0
wp_x, wp_y = 10, 1

def rotate(num, dir):
    global wp_x, wp_y
    tempNum = num
    gain = 1 if dir == 'R' else -1
    while num > 0:
        wp_x, wp_y = gain*wp_y, gain*-wp_x
        num -= 90

for line in lines:
    direction = line[0]
    extra = int(line[1:])

    if direction == 'R' or direction == 'L':
        rotate(extra, direction)
    elif direction == 'F':
        x += wp_x*extra
        y += wp_y*extra
    elif direction == 'N':
        wp_y += extra
    elif direction == 'S':
        wp_y -= extra
    elif direction == 'E':
        wp_x += extra
    elif direction == 'W':
        wp_x -= extra
    else:
        print('error')
        exit()

print(abs(x) + abs(y))