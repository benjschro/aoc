import re
import math

with open('../input/day14.txt') as file:
    lines = [line.strip() for line in file]

pattern = '^mem\[([0-9]+)\] = ([0-9]+)$'

def generate_binary(n):

  # 2^(n-1)  2^n - 1 inclusive
  bin_arr = range(0, int(math.pow(2,n)))
  bin_arr = [bin(i)[2:] for i in bin_arr]

  # Prepending 0's to binary strings
  max_len = len(max(bin_arr, key=len))
  bin_arr = [i.zfill(max_len) for i in bin_arr]

  return bin_arr

data = {}
mask = ''
for line in lines:
    if line[0:4] == 'mask':
        maskLine = line.split('=')
        mask = maskLine[1].strip()
    else:
        m = re.match(pattern, line, re.I)
        address = m.group(1)
        address = "{0:b}".format(int(address))
        addressNew = ''
        for idx, c in enumerate(reversed(mask)):
            if c == '1':
                addressNew += '1'
            elif c == 'X':
                addressNew += 'X'
            else:
                tmp = address[::-1]
                if idx < len(tmp):
                    addressNew += tmp[idx]
                else:
                    addressNew += '0'

        addressNew = addressNew[::-1]
        n = mask.count('X')
        arr = generate_binary(n)

        for a in arr:
            addressTemp = ''
            idx = 0
            success = True
            for c in reversed(addressNew):
                if c == 'X':
                    addressTemp += a[idx]
                    idx += 1
                else:
                    addressTemp += c

            data[int(addressTemp[::-1], 2)] = int(m.group(2))

sum = 0
for item in data:
    sum += data[item]


print(sum)