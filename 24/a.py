from collections import deque

input_list = open("input.txt", "r").readlines()

grid = []
for line in input_list:
    grid.append(line.replace("\n", ""))

ROW = len(grid)
COLUMN = len(grid[0])

row = 0
column = 0

while grid[row][column] == "#":
    column += 1

bad_cells = {}

for minute in range((ROW - 2) * (COLUMN - 2) + 1):
    bad = set()
    for r in range(ROW):
        for c in range(COLUMN):
            if grid[r][c] == ">":
                bad.add((r, 1 + ((c - 1 + minute) % (COLUMN - 2))))
            elif grid[r][c] == "v":
                bad.add((1 + ((r - 1 + minute) % (ROW - 2)), c))
            elif grid[r][c] == "<":
                bad.add((r, 1 + ((c - 1 - minute) % (COLUMN - 2))))
            elif grid[r][c] == "^":
                bad.add((1 + ((r - 1 - minute) % (ROW - 2)), c))
    bad_cells[minute] = bad


SEEN = set()
start = (row, column, 0, False, False)
Q = deque([start])

while Q:
    (row, column, minute, got_end, got_start) = Q.popleft()
    if not (0 <= row < ROW and 0 <= column < COLUMN and grid[row][column] != '#'):
        continue
    if row == ROW - 1:
        break
    if row == ROW - 1:
        got_end = True
    if row == 0 and got_end:
        got_start = True
    if(row, column, minute, got_start, got_end) in SEEN:
        continue
    SEEN.add((row, column, minute, got_start, got_end))
    BAD = bad_cells[minute + 1]

    if (row, column) not in BAD:
        Q.append((row, column, minute + 1, got_end, got_start))
    if (row + 1, column) not in BAD:
        Q.append((row + 1, column, minute + 1, got_end, got_start))
    if (row - 1, column) not in BAD:
        Q.append((row - 1, column, minute + 1, got_end, got_start))
    if (row, column + 1) not in BAD:
        Q.append((row, column + 1, minute + 1, got_end, got_start))
    if (row, column - 1) not in BAD:
        Q.append((row, column - 1, minute + 1, got_end, got_start))

print(minute)