import statistics

with open('../input/day7.txt') as file:
    myList = [line.strip() for line in file]

tmp = myList[0].split(',')

def solve(part):
    minimum = min(map(int, tmp))
    maximum = max(map(int, tmp))

    smallestSum = None
    for i in range(minimum, maximum + 1):
        sum = 0
        for item in tmp:
            if part == 1:
                sum += abs(int(item) - i)
            else:
                sum += abs(int(item) - i) * (abs(int(item) - i) + 1) // 2
        
        if smallestSum == None:
            smallestSum = sum
        elif sum < smallestSum:
            smallestSum = sum

    return smallestSum


print('partOne = ' + str(solve(1)))
print('partTwo = ' + str(solve(2)))

# $ python3 day7.py
# partOne = 341558
# partTwo = 93214037