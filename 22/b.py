input_list = open("input.txt", "r").readlines()

grid = []
orders = False

for line in input_list:
    if line == "\n":
        orders = True
    if orders:
        orders = line
    else:
        actual_line = []
        for char in line:
            if char != "\n":
                actual_line.append(char)
        grid.append(actual_line)


D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

row = len(grid)
column = len(grid[0])
for r in range(row):
    while len(grid[r]) < column:
        grid[r] += ' '

CUBE = column // 3

REGION = [(0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (3, 0)]

def regionToGlobal(r, c, region):
    rr, cc = REGION[region - 1]
    return (rr * CUBE + r, cc * CUBE + c)


def getRegion(r, c):
    for i,(rr, cc) in enumerate(REGION):
        if rr * CUBE <= r < ( rr + 1) * CUBE and cc * CUBE <= c < (cc + 1) * CUBE:
            return (i + 1, r - rr * CUBE, c - cc * CUBE)
    

def newCoords(r, c, d, nd):
    if d == 0:
        x = c
    if d == 1:
        x = r
    if d == 2:
        x = CUBE - 1 - c
    if d == 3:
        x = CUBE - 1 - r
    if nd == 0:
        return (CUBE - 1, x)
    if nd == 1:
        return (x, 0)
    if nd == 2:
        return (0, CUBE - 1 - x)
    if nd == 3:
        return (CUBE - 1 - x, CUBE - 1)


def getDest(r, c, d):
    region, rr, rc = getRegion(r, c)
    newRegion, nd = {
        (4,0):(3,0), (4,1):(2,3), (4,2):(6,3), (4,3):(5,3),
        (1,0):(6,1), (1,1):(2,1), (1,2):(3,2), (1,3):(5,1),
        (3,0):(1,0), (3,1):(2,0), (3,2):(4,2), (3,3):(5,2),
        (6,0):(5,0), (6,1):(4,0), (6,2):(2,2), (6,3):(1,2),
        (2,0):(6,0), (2,1):(4,3), (2,2):(3,3), (2,3):(1,3),
        (5,0):(3,1), (5,1):(4,1), (5,2):(6,2), (5,3):(1,1)
        }[(region, d)]

    nr, nc = newCoords(rr, rc, d, nd)
    nr, nc = regionToGlobal(nr, nc, newRegion)
    return (nr, nc, nd)


r = 0
c = 0
d = 1

while grid[r][c] != '.':
    c += 1

i = 0

while i < len(orders):
    n = 0
    while i < len(orders) and orders[i].isdigit():
        n = n * 10 + int(orders[i])
        i += 1
    for _ in range(n):
        rr = (r + D[d][0]) % row
        cc = (c + D[d][1]) % column
        if grid[rr][cc] == ' ':
            (nr, nc, nd) = getDest(r, c, d)
            if grid[nr][nc] == '#':
                break
            (r, c, d) = (nr, nc, nd)
            continue
        elif grid[rr][cc] == '#':
            break
        else:
            r = rr
            c = cc
    if i == len(orders):
        break
    turn = orders[i]
    if turn == 'L':
        d = (d + 3) % 4
    elif turn == 'R':
        d = (d + 1) % 4
    i += 1
    
DV = {0 : 3, 1 : 0, 2 : 1, 3 : 2}

print((r + 1) * 1000 + (c + 1) * 4 + DV[d])