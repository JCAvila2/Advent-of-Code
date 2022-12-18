input_list = open("input.txt", "r").readlines()

cubes = set()
for line in input_list:
    line = line.split(",")
    cubes.add((eval(line[0]), eval(line[1]), eval(line[2])))

grid = set()
for x, y, z in cubes:
    grid.add((x, y, z)) 

exposed_sides = 0

for (x, y, z) in grid:
    if (x - 1, y, z) not in grid:
        exposed_sides += 1
    if (x + 1, y, z) not in grid:
        exposed_sides += 1
    if (x, y - 1, z) not in grid:
        exposed_sides += 1
    if (x, y + 1, z) not in grid:
        exposed_sides += 1
    if (x, y, z - 1) not in grid:
        exposed_sides += 1
    if (x, y, z + 1) not in grid:
        exposed_sides += 1

print(exposed_sides)