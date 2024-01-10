from copy import deepcopy

original_input = open("input.txt", "r").read().strip().split("\n\n")
patterns = [[list(pattern) for pattern in pattern.split("\n")] for pattern in original_input]


def is_mirror(pattern, i):
    n, m = len(pattern), len(pattern[0])

    for r in range(m):
        for c in range(n):
            c2 = (i * 2) + 1 - c
            if not (0 <= c2 < n):
                continue
            if pattern[c][r] != pattern[c2][r]:
                return False
    return True


def get_new_pattern(pattern, avoid=(-1, -1)):
    n, m = len(pattern), len(pattern[0])

    h = -1
    for i in range(n - 1):
        if i != avoid[0] and is_mirror(pattern, i):
            h = i
            break

    v = -1
    vertical = list(zip(*pattern))
    for j in range(m - 1):
        if j != avoid[1] and is_mirror(vertical, j):
            v = j
            break

    return (h, v)


def get_pattern(pattern):
    n, m = len(pattern), len(pattern[0])
    summ_og = get_new_pattern(pattern)

    for i in range(n):
        for j in range(m):
            grid_copy = deepcopy(pattern)
            grid_copy[i][j] = "." if pattern[i][j] == "#" else "#"
            summ_new = get_new_pattern(grid_copy, avoid=summ_og)

            if summ_new not in [summ_og, (-1, -1)]:
                if summ_new[0] != -1:
                    return (summ_new[0] + 1) * 100
                else:
                    return summ_new[1] + 1


output = 0
for pattern in patterns:
    output += get_pattern(pattern)

print(output)
