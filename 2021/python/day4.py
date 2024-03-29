boards = []
numbers = None

def loadFile():
    global numbers

    with open('../input/day4.txt') as file:
        myList = [line.strip() for line in file]

    numbers = myList[0].split(',')

    for i in range(2, len(myList), 6):
        newBoard = []
        for j in range(0, 5):
            row = myList[i + j].replace('  ', ' ').split(' ')
            newBoard.append(row)

        boards.append(newBoard)

def checkWin(board):
    for row in board:
        if row.count('!') == 5:
            return True
    
    # Clever transpose I found on stackoverflow
    for row in map(list, map(None, *board)):
        if row.count('!') == 5:
            return True

    return False

winIdx = []
numIdx = []
def solve():
    for i in range(0, len(numbers)):
        for j in range(0, len(boards)):
            if j not in winIdx:
                b = boards[j]
                for k in range(0, len(b)):
                    row = b[k]
                    for m in range(0, len(row)):
                        boards[j][k][m] = '!' if row[m] == numbers[i] else row[m]

                if checkWin(b) is True:
                    winIdx.append(j)
                    numIdx.append(numbers[i])

def getScore(idx):
    sum = 0
    for row in boards[winIdx[idx]]:
        for col in row:
            if col != '!':
                sum += int(col)
    
    return sum * int(numIdx[idx])

loadFile()
solve()

print('partOne = ' + str(getScore(0)))
print('partTwo = ' + str(getScore(-1)))

# $ python3 day4.py
# partOne = 58374
# partTwo = 11377