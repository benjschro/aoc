with open('../input/day7.txt') as file:
    myList = [line.strip() for line in file]

tmp =  list(map(int, myList[0].split(',')))

def solve(part):
    smallestSum = None
    for i in range(min(tmp), max(tmp) + 1):
        sum = 0
        for item in tmp:
            if part == 1:
                sum += abs(item - i)
            else:
                sum += abs(item - i) * (abs(item - i) + 1) // 2
        
        if smallestSum == None or sum < smallestSum:
            smallestSum = sum

    return smallestSum

print('partOne = ' + str(solve(1)))
print('partTwo = ' + str(solve(2)))

# $ python3 day7.py
# partOne = 341558
# partTwo = 93214037