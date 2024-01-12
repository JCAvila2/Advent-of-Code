from copy import deepcopy

original_input = open("input.txt", "r").read().strip().split("\n")
original_input = [list(line) for line in original_input]
n, m = len(original_input), len(original_input[0])


def move_north(grid):
    n, m = len(grid), len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "O":
                ans += n - i
    return ans


def move_up(grid):
    n, m = len(grid), len(grid[0])
    
    for j in range(m):
        i = 0
        while i < n:
            while i < n and grid[i][j] == "#":
                i += 1

            start = i
            count = 0
            while i < n and grid[i][j] != "#":
                if grid[i][j] == "O":
                    count += 1
                i += 1

            for k in range(start, start + count):
                grid[k][j] = "O"
            for k in range(start + count, i):
                grid[k][j] = "."

    return grid


def rotate(grid):
    new_grid = [[None] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            new_grid[i][j] = grid[j][m - 1 - i]
    return new_grid


def rotateBy(grid, i):
    grid_copy = deepcopy(grid)
    for _ in range(i % 4):
        grid_copy = rotate(grid_copy)
    return grid_copy


def cycle(grid):
    grid_copy = deepcopy(grid)
    for i in range(4):
        grid_copy = rotateBy(grid_copy, 4 - (i % 4))
        grid_copy = move_up(grid_copy)
        grid_copy = rotateBy(grid_copy, i % 4)
    return grid_copy


history = {}
grid_cycle = {}
grid = original_input

for c in range(1000000000):
    grid = cycle(grid)

    H = "\n".join("".join(line) for line in grid)
    if H in history:
        time = c - history[H]
        ans_grid = grid_cycle[(1000000000 - 1 - history[H]) % time + history[H]]
        print(move_north(ans_grid))
        break

    history[H] = c
    grid_cycle[c] = deepcopy(grid) 
