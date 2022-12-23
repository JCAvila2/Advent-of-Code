import re

input_list = open("input.txt", "r").readlines()


def move(grid, actual_lo, n_moves, actual_dir):
    x = 0
    if actual_dir == ">":
        while x < n_moves:
            try:
                if grid[actual_lo[0]][actual_lo[1] + 1] == ".":
                    actual_lo = (actual_lo[0], actual_lo[1] + 1)
                elif grid[actual_lo[0]][actual_lo[1] + 1] == "#":
                    return actual_lo
                else:
                    for i in range(len(grid[actual_lo[0]])):
                        if grid[actual_lo[0]][i] == "#":
                            return actual_lo
                        if grid[actual_lo[0]][i] == ".":
                            actual_lo = (actual_lo[0], i)
                            break
            except:
                for i in range(len(grid[actual_lo[0]])):
                    if grid[actual_lo[0]][i] == "#":
                        return actual_lo
                    if grid[actual_lo[0]][i] == ".":
                        actual_lo = (actual_lo[0], i)
                        break
            x += 1
        return actual_lo

    elif actual_dir == "<":
        while x < n_moves:
            if (actual_lo[1] - 1) >= 0:
                if grid[actual_lo[0]][actual_lo[1] - 1] == ".":
                    actual_lo = (actual_lo[0], actual_lo[1] - 1)
                elif grid[actual_lo[0]][actual_lo[1] - 1] == "#":
                    return actual_lo
                else:
                    for i in range(len(grid[actual_lo[0]]), 0, -1):
                        try:
                            if grid[actual_lo[0]][i] == "#":
                                return actual_lo
                            if grid[actual_lo[0]][i] == ".":
                                actual_lo = (actual_lo[0], i)
                                break
                        except: 
                            pass
            else:
                for i in range(len(grid[actual_lo[0]]), 0, -1):
                    try:
                        if grid[actual_lo[0]][i] == "#":
                            return actual_lo
                        if grid[actual_lo[0]][i] == ".":
                            actual_lo = (actual_lo[0], i) 
                            break
                    except: 
                        pass
            x += 1
        return actual_lo

    elif actual_dir == "^":
        while x < n_moves:
            if (actual_lo[0] - 1) >= 0:
                if grid[actual_lo[0] - 1][actual_lo[1]] == ".":
                    actual_lo = (actual_lo[0] - 1, actual_lo[1])
                elif grid[actual_lo[0] - 1][actual_lo[1]] == "#":
                    return actual_lo
                else:
                    for t in range(len(grid), 0, -1):
                        try:
                            if grid[t][actual_lo[1]] == "#":
                                return actual_lo
                            if grid[t][actual_lo[1]] == ".":
                                actual_lo = (t, actual_lo[1])
                                break
                        except:
                            pass
            else:
                for t in range(len(grid), 0, -1):
                    try:
                        if grid[t][actual_lo[1]] == "#":
                            return actual_lo
                        if grid[t][actual_lo[1]] == ".":
                            actual_lo = (t, actual_lo[1])
                            break
                    except:
                        pass
            x += 1
        return actual_lo

    elif actual_dir == "v":
        while x < n_moves:
            try:
                if grid[actual_lo[0] + 1][actual_lo[1]] == ".":
                    actual_lo = (actual_lo[0] + 1, actual_lo[1])
                elif grid[actual_lo[0] + 1][actual_lo[1]] == "#":
                    return actual_lo
                else:
                    for i in range(len(grid)):
                        if grid[i][actual_lo[1]] == "#":
                            return actual_lo
                        if grid[i][actual_lo[1]] == ".":
                            actual_lo = (i, actual_lo[1]) 
                            break
            except:
                for i in range(len(grid)):
                    if grid[i][actual_lo[1]] == "#":
                        return actual_lo
                    if grid[i][actual_lo[1]] == ".":
                        actual_lo = (i, actual_lo[1]) 
                        break
            x += 1
        return actual_lo


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


orders_numbers = re.split("R|L|\s", orders)
orders_numbers = list(filter(lambda a: a != "", orders_numbers))
orders_letters = re.split("\d|\s", orders)
orders_letters = list(filter(lambda a: a != "", orders_letters))
actual_direction = ">"
actual_location = (0, 0)
for i in range(len(grid[0])):
    if grid[0][i] == ".":
        actual_location = (0, i)
        break


directions = [">", "v", "<", "^"]

for i in range(len(orders_letters)):
    actual_location = move(grid, actual_location, int(orders_numbers[i]), actual_direction)
    if orders_letters[i] == "R":
        new_dir_index = directions.index(actual_direction) + 1
        if new_dir_index <= 3:
            actual_direction = directions[new_dir_index]
        else:
            actual_direction = directions[0]
    else:
        new_dir_index = directions.index(actual_direction) - 1
        actual_direction = directions[new_dir_index]
actual_location = move(grid, actual_location, int(orders_numbers[i]), actual_direction)


if actual_direction == ">":
    facing = 0
elif actual_direction == "v":
    facing = 1
elif actual_direction == "<":
    facing = 2
else:
    facing = 3

print((1000 * (actual_location[0] + 1)) + (4 * (actual_location[1] + 1)) + facing)