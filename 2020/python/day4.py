import re

with open('../input/day4.txt') as file:
    lineArray = [line.strip() for line in file]

passportField = {
    'byr': '^(19[2-9][0-9]|200[0-2])$',
    'iyr': '^(201[0-9]|2020)$',
    'eyr': '^(202[0-9]|2030)$',
    'hgt': '^(((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)))$',
    'hcl': '^(#[0-9a-f]{6})$',
    'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': '^([0-9]{9})$'
}

numberOfValidPassports = [0, 0]
tempPassport = {}
lineIndex = 0

while True:
    if lineIndex >= len(lineArray) or len(lineArray[lineIndex].strip()) == 0:
        passportIsValid = [True, True]
        for key in passportField:
            if key in tempPassport:
                m = re.match(passportField[key], tempPassport[key], re.I)
                if m is None:
                    passportIsValid[1] = False
            else:
                passportIsValid[0] = False

        if passportIsValid[0]:
            numberOfValidPassports[0] = numberOfValidPassports[0] + 1        
            if passportIsValid[1]:
                numberOfValidPassports[1] = numberOfValidPassports[1] + 1
        
        if lineIndex >= len(lineArray):
            break

        tempPassport.clear()
    else:
        fields = lineArray[lineIndex].split()
        for keyValuePair in fields:
            key = keyValuePair.split(':')[0]
            value = keyValuePair.split(':')[1]
            tempPassport[key] = value
    lineIndex = lineIndex + 1

print('partOne = ' + str(numberOfValidPassports[0]))
print('partTwo = ' + str(numberOfValidPassports[1]))

# $ python3 day4.py
# partOne = 216
# partTwo = 150