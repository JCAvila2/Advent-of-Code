input_list = open("input.txt", "r").readlines()


def process(name, h):
    words = monkeys[name]
    if name == 'humn' and h >= 0:
        return h
    try:
        return int(words[0])
    except:
        e1 = process(words[0], h)
        e2 = process(words[2], h)
        return eval(str(e1) + words[1] + str(e2))

monkeys = {}

for line in input_list:
    line = line.split()
    name = line[0].replace(":", "")
    try:
        monkeys[name] = [line[1], line[2], line[3]]
    except:
        monkeys[name] = [line[1]]


p1 = monkeys['root'][0]
p2 = monkeys['root'][2]

if process(p2, 0) != process(p2, 1):
    p1, p2 = p2, p1

target = process(p2, 0)
lower = 0
higher = 100000000000000000000

while lower < higher:
    mid = (lower + higher) // 2
    score = target - process(p1, mid)
    if score < 0:
        lower = mid
    elif score == 0:
        break
    else:
        higher = mid

print(mid)