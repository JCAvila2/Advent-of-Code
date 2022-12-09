input_list = open("input.txt", "r")

h = (0, 0)
t = [(0, 0) for i in range(9)]
DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
rope = set([t[8]])

def move(H, T):
    dr = (H[0] - T[0])
    dc = (H[1] - T[1])
   
    if abs(dr) >= 2 and abs(dc) >= 2:
        if T[0] < H[0]:
            part1 = H[0] - 1
        else:
            part1 = H[0] + 1
        if T[1] < H[1]:
            part2 = H[1] - 1
        else:
            part2 = H[1] + 1
        T = (part1, part2)

    elif abs(dr) >= 2:
        if T[0] < H[0]:
            T = (H[0] - 1, H[1])
        else:
            T = (H[0] + 1, H[1])

    elif abs(dc) >= 2:
        if T[1] < H[1]:
            T = (H[0], H[1] - 1)
        else:
            T = (H[0], H[1] + 1)

    return T

for line in input_list:
    direction, distance = line.split()
    distance = int(distance)
    for m in range(distance):
        h = (h[0] + DR[direction], h[1] + DC[direction])
        t[0] = move(h, t[0])

        for i in range(1, 9):
            t[i] = move(t[i - 1], t[i])
        rope.add(t[8])

print(len(rope))