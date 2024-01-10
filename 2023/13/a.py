original_input = open("input.txt", "r").read().strip().split("\n\n")
patterns = [pattern.split("\n") for pattern in original_input]


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


output = 0
for pattern in patterns:
    n, m = len(pattern), len(pattern[0])

    h = -1
    for i in range(n - 1):
        if is_mirror(pattern, i):
            h = i
            break

    v = -1
    vertical = list(zip(*pattern))
    for j in range(m - 1):
        if is_mirror(vertical, j):
            v = j
            break

    output += v + 1 + 100 * (h + 1)


print(output)
