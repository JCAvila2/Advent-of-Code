input_list = open("input.txt", "r").readlines()

values = [1]

for line in input_list:
    line = line.split()

    values.append(values[-1])
    if line[0] == "addx":
        values.append(int(line[1]) + values[-1])

answer = 0
for x in range(20, 260, 40):
    answer += values[x-1] * x
print(answer)
