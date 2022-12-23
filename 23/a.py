from collections import defaultdict

input_list = open("input.txt", "r").readlines()

grid = []
elfs_pos = set()
dir_list = ['^', '>', 'v', '<']
rounds = 0


for line in input_list:
    actual_row = []
    for ch in line:
        if ch != "\n":
            actual_row.append(ch)
    grid.append(actual_row)


for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == "#":
            elfs_pos.add((row, column))


while rounds < 10:
    rounds += 1
    moving_elfs = defaultdict(list)

    for (row, column) in elfs_pos:
        alone = True
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (dr != 0 or dc != 0) and (row + dr, column + dc) in elfs_pos:
                    alone = False
        if alone:
            continue

        moved = False
        for d in dir_list:
            if d == "^" and (not moved) and (row - 1, column) not in elfs_pos and (row - 1, column - 1) not in elfs_pos and (row - 1, column + 1) not in elfs_pos:
                moving_elfs[(row - 1, column)].append((row, column))
                moved = True
            elif d == ">" and (not moved) and (row + 1, column) not in elfs_pos and (row + 1, column - 1) not in elfs_pos and (row + 1, column + 1) not in elfs_pos:
                moving_elfs[(row + 1, column)].append((row, column))
                moved = True
            elif d == "v" and (not moved) and (row, column - 1) not in elfs_pos and (row - 1, column - 1) not in elfs_pos and (row + 1, column - 1) not in elfs_pos:
                moving_elfs[(row, column - 1)].append((row, column))
                moved = True
            elif d == "<" and (not moved) and (row, column + 1) not in elfs_pos and (row - 1, column + 1) not in elfs_pos and (row + 1, column + 1) not in elfs_pos:
                moving_elfs[(row, column + 1)].append((row, column))
                moved = True

    dir_list = dir_list[1:] + [dir_list[0]]

    for new_pos, old_pos  in moving_elfs.items():
        if len(old_pos) == 1:
            elfs_pos.remove(old_pos[0])
            elfs_pos.add(new_pos)


row_min = min(row for (row, column) in elfs_pos)
row_max = max(row for (row, column) in elfs_pos)
column_min = min(column for (row, column) in elfs_pos)
column_max = max(column for (row, column) in elfs_pos)
answer = 0
for row in range(row_min, row_max + 1):
    for column in range(column_min, column_max + 1):
        if (row, column) not in elfs_pos:
            answer += 1
print(answer)