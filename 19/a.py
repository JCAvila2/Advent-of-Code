from collections import deque

input_list = open("input.txt", "r").readlines()


def solve(Co, Cc, Co1, Co2, Cg1, Cg2):
    best_option = 0
    S = (0, 0, 0, 0, 1, 0, 0, 0, 24)
    Q = deque([S])
    SEEN = set()
    
    while Q:
        state = Q.popleft()
        o, c, ob, g, r1, r2, r3, r4, t = state
        best_option = max(best_option, g)
        if t == 0:
            continue

        Core = max([Co, Cc, Co1, Cg1])
        if r1 >= Core:
            r1 = Core
        if r2 >= Co2:
            r2 = Co2
        if r3 >= Cg2:
            r3 = Cg2
        if o >= t * Core - r1 * (t - 1):
            o = t * Core - r1 * (t-1)
        if c >= t * Co2 - r2 * (t - 1):
            c = t * Co2 - r2 * (t - 1)
        if ob >= t * Cg2 - r3 * (t - 1):
            ob = t * Cg2 - r3 * (t - 1)

        state = (o, c, ob, g, r1, r2, r3, r4, t)

        if state in SEEN:
            continue
        SEEN.add(state)

        Q.append((o + r1, c + r2, ob + r3, g + r4, r1, r2, r3, r4, t - 1))
        if o >= Co:
            Q.append((o - Co + r1, c + r2, ob + r3, g + r4, r1 + 1, r2, r3, r4, t - 1))
        if o >= Cc:
            Q.append((o - Cc + r1, c + r2, ob + r3, g + r4, r1, r2 + 1, r3, r4, t - 1))
        if o >= Co1 and c >= Co2:
            Q.append((o - Co1 + r1, c - Co2 + r2, ob + r3, g + r4, r1, r2, r3 + 1, r4, t - 1))
        if o >= Cg1 and ob >= Cg2:
            Q.append((o- Cg1 + r1, c + r2, ob - Cg2 + r3, g + r4, r1, r2, r3, r4 + 1, t - 1))
    
    return best_option


answer = 0
for line in input_list:
    line = line.split(".")
    line = line[0].split(":") + line[1::]
    
    blueprint_number = int(line[0].split()[1])

    ore_price = int(line[1].split()[4])
    clay_price = int(line[2].split()[4])

    obsidian_ore_price = int(line[3].split()[4])
    obsidian_clay_price = int(line[3].split()[7])

    geode_ore_price = int(line[4].split()[4])
    geode_obsidian_price = int(line[4].split()[7])

    answer += blueprint_number * solve(ore_price, clay_price, obsidian_ore_price, obsidian_clay_price, geode_ore_price, geode_obsidian_price)
print(answer)