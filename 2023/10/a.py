from collections import deque

original_input = open("input.txt", "r").readlines()

S_pos = None
n, m = len(original_input), len(original_input[0])


for row in range(len(original_input)):
    for col in range(len(original_input[row])):
        if original_input[row][col] == "S":
            S_pos = (row, col)
            break
    if S_pos != None:
        break


def get_nbr(r, c):
    res = []
    for dr, dc in get_neighbors(r, c):
        rr, cc = r + dr, c + dc
        if not (0 <= rr < n and 0 <= cc < m):
            continue
        res.append((rr, cc))
    return res


def get_neighbors(r, c):
    res = []
    if (r, c) == S_pos:
        for sr, sc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr, cc = r + sr, c + sc
            if not (0 <= rr < n and 0 <= cc < m):
                continue
            
            if (r, c) in get_nbr(rr, cc):
                res.append((sr, sc))
        return res
    else:
        res = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            ".": []
        }
        return res[original_input[r][c]]


# BFS
visited = set()
distances = {}
q = deque([(S_pos, 0)])
while q:
    top, distance = q.popleft()
    if top in visited:
        continue
    visited.add(top)
    distances[top] = distance
    for nbr in get_nbr(*top):
        if nbr in visited:
            continue
        q.append((nbr, distance + 1))

print(max(distances.values()))
