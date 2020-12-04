with open('../input/day2.txt') as file:
    dimensionList = [line.strip() for line in file]

sqft = 0
ribbon = 0
for dimension in dimensionList:
    l = int(dimension.split('x')[0])
    w = int(dimension.split('x')[1])
    h = int(dimension.split('x')[2])

    sqft += 2*l*w + 2*w*h + 2*h*l
    sqft += min(l*w, w*h, h*l)

    ribbon += 2*l + 2*w + 2*h
    ribbon -= max(2*l, 2*w, 2*h)
    ribbon += l*w*h


print('partOne = ' + str(sqft))
print('partTwo = ' + str(ribbon))

# $ python3 day2.py
# partOne = 1588178
# partTwo = 3783758