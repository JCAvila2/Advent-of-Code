original_input = open("input.txt", "r").read().strip().split("\n\n")

part1, part2 = original_input[0].split("\n"), original_input[1].split("\n")
workflows = {}
output = 0


def acceptItem(item, name='in'):
    if name == 'R':
        return False
    if name == 'A':
        return True
    rules, fallback = workflows[name]
    for key, cmp, n, target in rules:
        if eval(f"{item[key]} {cmp} {n}"):
            return acceptItem(item, target)
    return acceptItem(item, fallback)


for line in part1:
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        c, t = rule.split(":")
        key = c[0]
        cmp = c[1]
        n = int(c[2:])
        workflows[name][0].append((key, cmp, n, t))

for line in part2:
    item = {}
    for segment in line[1:-1].split(","):
        ch, n = segment.split("=")
        item[ch] = int(n)
    if acceptItem(item):
        output += sum(item.values())

print(output)
