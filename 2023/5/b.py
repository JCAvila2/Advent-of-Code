original_input = open("input.txt", "r").readlines()
ranges_of_seeds = original_input[0].replace("seeds: ", "").replace("\n", "").split(" ")

seeds = []
instructions = []
actual = []

for r in range(0, len(ranges_of_seeds), 2):
    start = int(ranges_of_seeds[r])
    end = start + int(ranges_of_seeds[r + 1])
    seeds.append((start, end))

for line in range(2, len(original_input)):
    if original_input[line][0].isdigit():
        actual.append(list(map(int, original_input[line].split(" "))))
    else:
        if len(actual) > 0:
            instructions.append(actual)
            actual = []
    if line == len(original_input) - 1:
        instructions.append(actual)


for block in instructions:
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in block:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if oe < e:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
