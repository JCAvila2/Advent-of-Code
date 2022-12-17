input_list = open("input.txt", "r").readlines()


def move_rock(grid, rock_pos, direction):
    new_rock_pos = []
    if direction == "<":
        for r in rock_pos:
            if r[1] == 0: 
                return rock_pos
            try:
                if grid[r[0]][r[1] - 1] == "#":
                    return rock_pos
                new_rock_pos.append((r[0], r[1] - 1))
            except:
                return rock_pos

        return new_rock_pos

    elif direction == ">":
        for r in rock_pos:
            if r[1] == 6: 
                return rock_pos
            try:
                if grid[r[0]][r[1] + 1] == "#":
                    return rock_pos
                new_rock_pos.append((r[0], r[1] + 1))
            except:
                return rock_pos

        return new_rock_pos

    else: 
        for r in rock_pos:
            try:
                if grid[r[0] + 1][r[1]] == "#":
                    return False
                new_rock_pos.append((r[0] + 1, r[1]))
            except: 
                return False
        
        return new_rock_pos


gas = input_list[0]
grid = []
actual_rock_type = 0
actual_gas_dir = 0
actual_rock_pos = []
actual_rock_height = 0
moves = 0
rocks_droped = 0

while rocks_droped < 2022:
    rocks_droped += 1

    for g in range(3):
        grid.insert(0, [" " for _ in range(7)])


    if actual_rock_type == 0:
        actual_rock_pos = [(0, 2), (0, 3), (0, 4), (0, 5)]
        actual_rock_height = 1
    elif actual_rock_type == 1:
        actual_rock_pos = [(0, 3), (1, 3), (2, 3), (1, 2), (1, 4)] 
        actual_rock_height = 3
    elif actual_rock_type == 2:
        actual_rock_pos = [(0, 4), (1, 4), (2, 4), (2, 3), (2, 2)]
        actual_rock_height = 3
    elif actual_rock_type == 3:
        actual_rock_pos = [(0, 2), (1, 2), (2, 2), (3, 2)]
        actual_rock_height = 4
    elif actual_rock_type == 4:
        actual_rock_pos = [(0, 2), (1, 2), (0, 3), (1, 3)]
        actual_rock_height = 2


    for r in range(actual_rock_height):
        grid.insert(0, [" " for _ in range(7)])

    while True:
        if moves % 2 == 0:
            m = move_rock(grid, actual_rock_pos, gas[actual_gas_dir])
            actual_gas_dir += 1
        else:
            m = move_rock(grid, actual_rock_pos, "D")
        moves += 1
        if actual_gas_dir == len(gas):
            actual_gas_dir = 0

        if m:
            actual_rock_pos = m
        else:
            break

    for ar in actual_rock_pos:
        grid[ar[0]][ar[1]] = "#"

    while True:
        if "#" in grid[0]:
            break
        else:
            grid.pop(0)

    actual_rock_type += 1 
    if actual_rock_type == 5:
        actual_rock_type = 0
    
print(len(grid))