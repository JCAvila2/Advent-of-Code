from collections import deque

original_input = open("input.txt", "r").read().strip().split("\n")

positions = [(0, -1, 0, 1)]
seen = set()
q = deque(positions)
n, m = len(original_input), len(original_input[0])

while q:
    r, c, dr, dc = q.popleft()

    r += dr
    c += dc

    if r < 0 or r >= n or c < 0 or c >= m:
        continue

    char = original_input[r][c]
    
    if char == '.' or (char == '-' and dc != 0) or (char == '|' and dr != 0):
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))
    elif char == "/":
        dr, dc = -dc, -dr
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))
    elif char == "\\":
        dr, dc = dc, dr
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))        
    elif char == "|":
        for dr, dc in [(1, 0), (-1, 0)]:
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
    else:
        for dr, dc in [(0, 1), (0, -1)]:
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))


coordinates = set()
for (r, c, dr, dc) in seen:
    coordinates.add((r, c))

print(len(coordinates))
