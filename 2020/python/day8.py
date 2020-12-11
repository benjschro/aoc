class myComputer:

    def __init__(self, inputPath):
        self.instructions = []
        self.traceBuffer = []
        self.inputPath = inputPath
        self.reset()

    def _loadInstructions(self):
        fp = open(self.inputPath, 'r')
        for line in fp:
            opcode = line.split()[0]
            operand1 = int(line.split()[1])
            self.instructions.append((opcode, operand1))
    
    def reset(self):
        self.instructions.clear()
        self.traceBuffer.clear()
        self.pc = 0
        self.acc = 0
        self.halted = False
        self._loadInstructions()
    
    def step(self):
        # don't continue if the computer is halted
        if self.halted:
            print('cannot run cpu when it is halted')
            exit()
            return

        # check if pc points within the program memory
        if self.pc < 0 or self.pc > len(self.instructions) - 1:
            self.halted = True
            return

        # all instructions have an opcode, so pull it out
        opcode = self.instructions[self.pc][0]

        # all instructions have at least a single operand, so pull it out
        operand1 = self.instructions[self.pc][1]

        pcDiff = 0
        if opcode == 'acc':
            self.acc += operand1
            pcDiff = 1
        elif opcode == 'jmp':
            pcDiff += operand1
        elif opcode == 'nop':
            pcDiff = 1
        else:
            print('invalid instruction - halting cpu')
            print(opcode)
            self.halted = True
        
        # traceInfo format is (pc, opcode, operand1, operand1, ...)
        traceInfo = (self.pc,)
        traceInfo += self.instructions[self.pc]
        self.traceBuffer.append(traceInfo)
        self.pc += pcDiff
    
    def run(self):
        while not self.halted:
            self.step()

x = myComputer('../input/day8.txt')

repeatedInstruction = False
while not repeatedInstruction:
    instruction = x.instructions[x.pc]
    if (x.pc,) + instruction in x.traceBuffer:
        repeatedInstruction = True
    else:
        x.step()

print('partOne = ' + str(x.acc))

y = myComputer('../input/day8.txt')
for count, instruction in enumerate(x.instructions):
    y.reset()
    if instruction[0] == 'jmp':
        y.instructions[count] = ('nop', y.instructions[count][1])
    elif instruction[0] == 'nop':
        y.instructions[count] = ('jmp', y.instructions[count][1])

    while len(y.traceBuffer) < 5000 and not y.halted:
        y.step()
    
    if y.pc == len(y.instructions):
        break

print('partTwo = ' + str(y.acc))