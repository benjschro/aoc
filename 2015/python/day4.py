import hashlib
import re

with open('../input/day4.txt') as file:
    input = file.readline()

patternOne = '^0{5}.*$'
patternTwo = '^0{6}.*$'

partOneAnswer = 0
partTwoAnswer = 0
counter = 1
while True:
    hashInput = input + str(counter)
    hash = hashlib.md5(hashInput.encode('utf-8')).hexdigest()

    m = re.match(patternOne, hash, re.I)
    if m is not None and partOneAnswer == 0:
        partOneAnswer = counter

    m = re.match(patternTwo, hash, re.I)
    if m is not None and partTwoAnswer == 0:
        partTwoAnswer = counter
        break

    counter += 1

print('partOne = ' + str(partOneAnswer))
print('partTwo = ' + str(partTwoAnswer))

# $ time python3 day4.py
# partOne = 117946
# partTwo = 3938038

# real    0m16.328s
# user    0m0.000s
# sys     0m0.015s