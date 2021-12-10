with open('../input/day10.txt') as file:
    myList = [line.strip() for line in file]

openChars = ['(', '[', '{', '<']
closeChars = [')', ']', '}', '>']
scores = [3, 57, 1197, 25137]
addScores = [1, 2, 3, 4]
stack = []

score = 0
part2scores = []
for line in myList:
    stack.clear()
    for c in line:
        if c in openChars:
            stack.append(c)
        else:
            openC = stack.pop()
            idx = openChars.index(openC)
            expectedC = closeChars[idx]
            if c != expectedC:
                foundIdx = closeChars.index(c)
                score += scores[foundIdx]
                stack.clear()
                break
    
    if len(stack) > 0:
        newestScore = 0
        while len(stack) > 0:
            item = stack.pop()
            idx = openChars.index(item)
            newestScore *= 5
            newestScore += addScores[idx]
        part2scores.append(newestScore)

print('partOne = ' + str(score))
print('partTwo = ' + str(sorted(part2scores)[(len(part2scores) // 2)]))

# $ python3 day10.py
# partOne = 411471
# partTwo = 3122628974