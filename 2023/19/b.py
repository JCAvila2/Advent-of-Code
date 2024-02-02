original_input = open("input.txt", "r").read().strip().split("\n\n")

part1, part2 = original_input[0].split("\n"), original_input[1].split("\n")
workflows = {}
output = 0


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


def count(ranges, name='in'):
    if name == 'R':
        return 0
    if name == 'A':
        product = 1
        for l, h in ranges.values():
            product *= h - l + 1
        return product
    rules, fallback = workflows[name]
    total = 0
    for key, cmp, n, target in rules:
        l, h, =  ranges[key]
        if cmp == '<':
            t = (l, n - 1)
            f = (n, h)
        else:
            t = (n + 1, h)
            f = (l, n)
        if t[0] <= t[1]:
            copy = dict(ranges)
            copy[key] = t
            total += count(copy, target)
        if f[0] <= f[1]:
            ranges = dict(ranges)
            ranges[key] = f
        else:
            break
    else:
        total += count(ranges, fallback)
    return total


print(count({key: (1, 4000) for key in 'xmas'}))
