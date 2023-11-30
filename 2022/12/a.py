input_list = open("input.txt", "r").readlines()


def path_finding(grid, ending_position, min_steps):
    queue = [ending_position]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(queue) > 0:
        curr = queue.pop(0)
        actual_row = curr[0]
        actual_column = curr[1]
        for dir in directions:
            next_row = actual_row + dir[0]
            next_column = actual_column + dir[1]
            if next_row < 0 or next_column < 0 or next_row >= len(grid) or next_column >= len(grid[0]):
                continue
            if grid[actual_row][actual_column] <= grid[next_row][next_column] + 1 and (next_row, next_column) not in min_steps:
                min_steps[(next_row, next_column)] = curr[2] + 1
                queue.append((next_row, next_column, curr[2] + 1)) 
    return min_steps


grid = []
for row in input_list:
    row = [char for char in row if char != "\n"]
    grid.append(row)


for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == "S":
            starting_point = (row, column, 1)
            grid[row][column] = 0
        elif grid[row][column] == "E":
            ending_point = (row, column, 0)
            grid[row][column] = 25
        else:
            grid[row][column] = ord(grid[row][column]) - ord('a')


min_steps = dict(ending_point = 0)
min_steps = path_finding(grid, ending_point, min_steps)
print(min_steps[(starting_point[0], starting_point[1])])