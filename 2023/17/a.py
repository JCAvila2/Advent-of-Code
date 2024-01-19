from heapq import heappush, heappop

original_input = open("input.txt", "r").read().strip().split("\n")
n, m = len(original_input), len(original_input[0])

for line in range(n):
    original_input[line] = list(map(int, original_input[line].strip()))

seen = set()
priority_q = [(0, 0, 0, 0, 0, 0)]

while priority_q:
    hl, r, c, dr, dc, nt = heappop(priority_q)

    if r == n - 1 and c == m - 1:
        print(hl)
        break

    if (r, c, dr, dc, nt) in seen:
        continue

    seen.add((r, c, dr, dc, nt))
    
    if nt < 3 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            heappush(priority_q, (hl + original_input[nr][nc], nr, nc, dr, dc, nt + 1))

    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
            nr = r + ndr
            nc = c + ndc
            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                heappush(priority_q, (hl + original_input[nr][nc], nr, nc, ndr, ndc, 1))
