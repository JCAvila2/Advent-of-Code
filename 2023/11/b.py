original_input = open("input.txt", "r").read().strip().split("\n")

galaxies = []
for row in range(len(original_input)):
    for col in range(len(original_input[row])):
        if original_input[row][col] == "#":
            galaxies.append((row, col))

empty_rows = []
for row in range(len(original_input)):
    empty_rows.append("#" not in original_input[row])

empty_cols = []
for col in range(len(original_input[0])):    
    valid = True
    for row in range(len(original_input)):
        if original_input[row][col] == "#":
            valid = False
            break
    empty_cols.append(valid)


def get_dist(a, b):
    dis = 0
    ra, ca = a
    rb, cb = b

    if ra > rb:
        ra, rb = rb, ra
    if ca > cb:
        ca, cb = cb, ca


    for row in range(ra, rb):
        dis += 1
        if empty_rows[row]:
            dis += 1000000 - 1

    for col in range(ca, cb):
        dis += 1
        if empty_cols[col]:
            dis += 1000000 - 1

    return dis
    

output = 0
for g1 in range(len(galaxies)):
    for g2 in range(g1 + 1, len(galaxies)):
        output += get_dist(galaxies[g1], galaxies[g2])

print(output)
