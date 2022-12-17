input_list = open("input.txt", "r").readlines()


def get_rock(t, y):
    if t == 0:
        return set([(2, y), (3, y), (4, y), (5, y)])
    elif t == 1:
        return set([(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)])
    elif t == 2:
        return set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)])
    elif t == 3:
        return set([(2, y), (2, y + 1), (2, y + 2), (2, y + 3)])
    elif t == 4:
        return set([(2, y + 1), (2, y), (3, y + 1), (3, y)])


def move_left(piece):
    if any([x == 0 for (x, y) in piece]):
        return piece
    return set([(x - 1, y) for (x, y) in piece])


def move_right(piece):
    if any([x == 6 for (x, y) in piece]):
        return piece
    return set([(x + 1, y) for (x, y) in piece])


def move_down(piece):
    return set([(x, y - 1) for (x, y) in piece])


def move_up(piece):
    return set([(x, y + 1) for (x, y) in piece])
 

def signature(R):
    maxY = max([y for (x, y) in R])
    return frozenset([(x, maxY - y) for (x, y) in R if maxY - y <= 30])


R = set([(x, 0) for x in range(7)])
gas = input_list[0]
SEEN = {}
top = 0
actual_rock_type = 0
rocks_droped = 0
added = 0
TOTAL_ROCKS = 1000000000000

while rocks_droped < TOTAL_ROCKS:
    piece = get_rock(rocks_droped % 5, top + 4)
    while True:
        if gas[actual_rock_type] == '<':
            piece = move_left(piece)
            if piece & R:
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & R:
                piece = move_left(piece)
        actual_rock_type = (actual_rock_type + 1) % len(gas)
        piece = move_down(piece)
        if piece & R:
            piece = move_up(piece)
            R |= piece
            top = max([y for (x, y) in R])
            SR = (actual_rock_type, rocks_droped % 5, signature(R))
            if SR in SEEN and rocks_droped  >= 2022:
                (oldt, oldy) = SEEN[SR]
                dy = top - oldy
                dt = rocks_droped - oldt
                amt = (TOTAL_ROCKS - rocks_droped) // dt
                added += amt * dy
                rocks_droped  += amt * dt
            SEEN[SR] = (rocks_droped ,top)
            break
    rocks_droped += 1

print(top + added)