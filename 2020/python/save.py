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
                rejectList.append(int(item))

print(ranges)
print(rejectList)

sum = 0
for item in rejectList:
    sum += item
print(sum)