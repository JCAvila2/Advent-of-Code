from collections import deque

original_input = open("input.txt", "r").read().strip().split("\n")
n, m = len(original_input), len(original_input[0])


def get_tiles(r, c, dr, dc):
    positions = [(r, c, dr, dc)]
    seen = set()
    q = deque(positions) 

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
    return len(coordinates)


max_value = 0

for row in range(n):
    max_value = max(max_value, get_tiles(row, -1, 0, 1))
    max_value = max(max_value, get_tiles(row, m, 0, -1))

for col in range(n):
    max_value = max(max_value, get_tiles(-1, col, 1, 0))
    max_value = max(max_value, get_tiles(n, col, -1, 0))

print(max_value)
