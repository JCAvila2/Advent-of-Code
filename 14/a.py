input_list = open("input.txt", "r").readlines()


list_of_rocks = set()
limit_x_min = float('inf')
limit_x_max = 0
limit_y = 0

for line in input_list:
    line = line.split("->")
    for i in range(len(line) - 1):
        pos1 = eval(line[i])
        pos2 = eval(line[i + 1])
        if pos1[0] == pos2[0]:
            if pos1[1] < pos2[1]:
                for rock in range(pos1[1], pos2[1] + 1):
                    list_of_rocks.add((pos1[0], rock))
            else:
                for rock in range(pos1[1], pos2[1] - 1, -1):
                    list_of_rocks.add((pos1[0], rock))
        else:
            if pos1[0] < pos2[0]:
                for rock in range(pos1[0], pos2[0] + 1):
                    list_of_rocks.add((rock, pos1[1]))
            else:
                for rock in range(pos1[0], pos2[0] - 1, -1):
                    list_of_rocks.add((rock, pos1[1]))
        if max(pos1[1], pos2[1]) > limit_y: 
            limit_y = max(pos1[1], pos2[1])
        if min(pos1[0], pos2[0]) < limit_x_min:
            limit_x_min = min(pos1[0], pos2[0])
        if max(pos1[0], pos2[0]) > limit_x_max:
            limit_x_max = max(pos1[0], pos2[0])


def drop_sand(list_of_r, list_of_s, actual_pos):
    global limit_x_min, limit_x_max, limit_y
    while actual_pos[1] < limit_y and actual_pos[0] in range(limit_x_min, limit_x_max):
        if (actual_pos[0], actual_pos[1] + 1) not in list_of_r and (actual_pos[0], actual_pos[1] + 1) not in list_of_s:
            actual_pos = (actual_pos[0], actual_pos[1] + 1)
        elif (actual_pos[0] - 1, actual_pos[1] + 1) not in list_of_r and (actual_pos[0] - 1, actual_pos[1] + 1) not in list_of_s:
            actual_pos = (actual_pos[0] - 1, actual_pos[1] + 1)
        elif (actual_pos[0] + 1, actual_pos[1] + 1) not in list_of_r and (actual_pos[0] + 1, actual_pos[1] + 1) not in list_of_s:
            actual_pos = (actual_pos[0] + 1, actual_pos[1] + 1)
        else:
            return actual_pos
    return actual_pos


list_of_sand = set()
starting_pos = (500, 0)
while True:
    sand_pos = drop_sand(list_of_rocks, list_of_sand, starting_pos)
    if sand_pos[0] in range(limit_x_min, limit_x_max) and sand_pos[1] < limit_y:
        list_of_sand.add(sand_pos)
    else:
        break

print(len(list_of_sand))