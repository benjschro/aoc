with open('../input/day18.txt') as file:
    lines = [line.strip() for line in file]

def parse(expr):
    stack = [[]]
    for i in expr:
        current_node = stack[-1]
        if i == '(':
            new_node = []
            current_node.append(new_node)
            stack.append(new_node)
        elif i == ')':
            stack.pop()
        elif not i.isspace():
            current_node.append(i)

    return stack[0]

def performOp(x, y, sign):
    ret = 0

    if sign == '*':
        ret = int(x) * int(y)
    elif sign == '+':
        ret = int(x) + int(y)

    return ret


def unrollList(inputList):
    # ret = 0
    lastNum = None
    lastSign = None

    multList = []
    for item in inputList:
        if isinstance(item, list):
            tmp = unrollList(item)
            if lastNum == None:
                lastNum = tmp
            else:
                tmp2 = performOp(lastNum, tmp, lastSign)
                lastNum = tmp2
                lastSign = None
        elif item == '+':
            lastSign = item
        elif item == '*':
            multList.append(int(lastNum))
            lastNum = None
        else:
            if lastNum == None:
                lastNum = item
            else:
                tmp = performOp(lastNum, item, lastSign)
                lastNum = tmp
                lastSign = None
    multList.append(int(lastNum))
    ret = 1
    for item in multList:
        ret *= item
    return ret

value = 0

sum = 0
for line in lines:
    sp = parse(line)
    sum += unrollList(sp)
    # break

print(sum)
