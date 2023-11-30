from collections import deque

input_list = open("input.txt", "r").readlines()

cubes = set()
for line in input_list:
    line = line.split(",")
    cubes.add((eval(line[0]), eval(line[1]), eval(line[2])))


OUT = set()
IN = set()


def reaches_outside(x, y, z):
    
    if (x, y, z) in OUT:
        return True
    elif (x, y, z) in IN:
        return False


    SEEN = set()
    Q = deque([(x, y, z)])

    while Q:
        x, y, z = Q.popleft()
        if (x, y, z) in cubes or (x, y, z) in SEEN:
            continue
        
        SEEN.add((x, y, z))

        if len(SEEN) > 5000:
            for p in SEEN:
                OUT.add(p)
            return True

        Q.append((x + 1, y, z))
        Q.append((x - 1, y, z))
        Q.append((x, y + 1, z))
        Q.append((x, y - 1, z))
        Q.append((x, y, z + 1))
        Q.append((x, y, z - 1))

    for p in SEEN:
        IN.add(p)

    return False



sides_exposed = 0
for (x, y, z) in cubes:
    if reaches_outside(x + 1, y, z):
        sides_exposed += 1
    if reaches_outside(x - 1, y, z):
        sides_exposed += 1
    if reaches_outside(x, y + 1, z):
        sides_exposed += 1
    if reaches_outside(x, y - 1, z):
        sides_exposed += 1
    if reaches_outside(x, y, z + 1):
        sides_exposed += 1
    if reaches_outside(x, y, z - 1):
        sides_exposed += 1

print(sides_exposed)