original_input = open("input.txt").read().strip().split("\n")

actual_pos = (0, 0)
ground = [(0, 0)]

B = 0
for line in original_input:
    direction, distance, color = line.split(" ")
    distance = int(distance)
    B += distance
    if direction == "U":
        actual_pos = (actual_pos[0] - distance, actual_pos[1]) 
    elif direction == "D":
        actual_pos = (actual_pos[0] + distance, actual_pos[1])
    elif direction == "R":
        actual_pos = (actual_pos[0], actual_pos[1] + distance)
    elif direction == "L":
        actual_pos = (actual_pos[0], actual_pos[1] - distance)

    ground.append(actual_pos)

A = 0
for i in range(len(ground)):
    A += ground[i][0] * (ground[i - 1][1] - ground[(i + 1) % len(ground)][1])
A = abs(A) / 2
I = A - B // 2 + 1
print(int(B + I))
