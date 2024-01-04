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


loop = {(S_pos)}
q = deque([(S_pos)])
maybe_s = {"|", "-", "J", "L", "7", "F"}

while q:
    r, c = q.popleft()
    ch = original_input[r][c]

    if r > 0 and ch in "S|JL" and original_input[r - 1][c] in "|7F" and (r - 1, c) not in loop:
        loop.add((r - 1, c))
        q.append((r - 1, c))
        if ch == "S":
            maybe_s &= {"|", "J", "L"}
        
    if r < n - 1 and ch in "S|7F" and original_input[r + 1][c] in "|JL" and (r + 1, c) not in loop:
        loop.add((r + 1, c))
        q.append((r + 1, c))
        if ch == "S":
            maybe_s &= {"|", "7", "F"}

    if c > 0 and ch in "S-J7" and original_input[r][c - 1] in "-LF" and (r, c - 1) not in loop:
        loop.add((r, c - 1))
        q.append((r, c - 1))
        if ch == "S":
            maybe_s &= {"-", "J", "7"}

    if c < n - 1 and ch in "S-LF" and original_input[r][c + 1] in "-J7" and (r, c + 1) not in loop:
        loop.add((r, c + 1))
        q.append((r, c + 1))
        if ch == "S":
            maybe_s &= {"-", "L", "F"}


(S,) = maybe_s
original_input[S_pos[0]] = original_input[S_pos[0]].replace("S", S)
original_input = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(original_input)]
outside = set()

for r, row in enumerate(original_input):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            within = not within
        elif ch in "LF":
            up = ch == "L"
        elif ch in "7J":
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass

        if not within:
            outside.add((r, c))
            
print(n * m - len(outside | loop))
