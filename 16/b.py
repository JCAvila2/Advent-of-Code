input_list = open("input.txt", "r").readlines()


valves = {}
best = 0

for line in input_list:
    line = line.split()
    flow_rate = line[4].split("=")[1].replace(";", "") 
    leads_to = []
    for i in range(len(line)-1, 8, -1):
        leads_to.append(line[i].replace(",", ""))
    valves[line[1]] = {"flow" : int(flow_rate), "tunnels" : leads_to, "paths" : {}}

keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])


def bfs(frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            for y in valves[x]['tunnels']:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1


for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)



def search(opened, flowed, current_room, depth_to_go, elephants_turn):
    global best
    if flowed > best:
        best = flowed

    if depth_to_go <= 0:
        return

    if current_room not in opened:
        search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
        if not elephants_turn:
            search(set([current_room]).union(opened), flowed + valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
    else:
        for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
            search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k], elephants_turn)

search(set(['AA']), 0, 'AA', 25, False)
print(best)