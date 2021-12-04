import re

boards = []
numbers = None

def loadFile():
    global boards
    global numbers

    with open('../input/day4.txt') as file:
        myList = [line.strip() for line in file]

    numbers = myList[0].split(',')

    stringPattern = '^[0-9]+\s+[0-9]+\s+[0-9]+\s+[0-9]+\s+[0-9]+'

    newBoard = False
    for i in range(2, len(myList), 6):
        newBoard = []
        for j in range(0, 5):
            m = re.match(stringPattern, myList[i+j])
            newBoard.append([x for x in m.group(0).split(' ') if x != ''])

        boards.append(newBoard)

def checkWin(board):
    for row in board:
        if row == ['!', '!', '!', '!', '!']:
            return True
    
    for col in range(0, len(board[0])):
        if board[0][col] == '!' and \
            board[1][col] == '!' and \
            board[2][col] == '!' and \
            board[3][col] == '!' and \
            board[4][col] == '!':
            return True

    return False

winIdx = []
numIdx = []
def solveIndex():
    global boards
    global numbers

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
    global boards

    sum = 0
    for row in boards[winIdx[idx]]:
        for col in row:
            if col != '!':
                sum += int(col)
    
    return sum * int(numIdx[idx])

loadFile()
solveIndex()

print('partOne = ' + str(getScore(0)))
print('partTwo = ' + str(getScore(-1)))
