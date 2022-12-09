input_list = open("input.txt", "r").readlines()

head_position = (0, 0)
tail_position = (0, 0)
t_pos = set()

def move_tail(head_position, tail_position):
    if abs(head_position[0] - tail_position[0]) >= 2:
        if head_position[0] > tail_position[0]:
            tail_position = (tail_position[0] + 1, head_position[1])
        else: 
            tail_position = (tail_position[0] - 1, head_position[1])
    if abs(head_position[1] - tail_position[1]) >= 2:
        if head_position[1] > tail_position[1]:
            tail_position = (head_position[0], tail_position[1] + 1)
        else:
            tail_position = (head_position[0], tail_position[1] - 1)

    return tail_position

def move(direction, distance, head_position, tail_position, t_pos):
    for move in range(int(distance)):
        if direction == "U":
            head_position = (head_position[0] - 1, head_position[1])
        elif direction == "D":
            head_position = (head_position[0] + 1, head_position[1])
        elif direction == "L":   
            head_position = (head_position[0], head_position[1] - 1)
        elif direction == "R":
            head_position = (head_position[0], head_position[1] + 1)
        tail_position = move_tail(head_position, tail_position)
        t_pos.add(tail_position)
    return head_position, tail_position, t_pos

for line in input_list:
    line = line.split()
    head_position, tail_position, t_pos = move(line[0], line[1], head_position, tail_position, t_pos)
    
print(len(t_pos))