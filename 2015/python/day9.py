import re
import itertools

with open('../input/day9.txt') as file:
    lines = [line.strip() for line in file]

pattern = '^(.*) to (.*) = (.*)$'
routes = {}
destinations = set()
for line in lines:
    m = re.match(pattern, line, re.I)
    routes[(m.group(1), m.group(2))] = int(m.group(3))
    destinations.add(m.group(1))
    destinations.add(m.group(2))

possibleRoutes = list(itertools.permutations(destinations))

routeMin = 999999999
routeMax = 0
for route in possibleRoutes:
    tmpSum = 0
    for i in range(0, len(route) - 1):
        key1 = (route[i], route[i+1])
        key2 = (route[i+1], route[i])
        if key1 in routes:
            tmpSum += routes[key1]
        elif key2 in routes:
            tmpSum += routes[key2]
        else:
            tmpSum = 999999999
            break

    routeMin = min(routeMin, tmpSum)
    routeMax = max(routeMax, tmpSum)

    

print(routeMin)
print(routeMax)

# $ python3 tmp.py
# shortest: 251
# longest: 898

# 464 too high