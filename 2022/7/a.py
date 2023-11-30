input_list = open("input.txt", "r").readlines()

actual_directory = []
answer = 0

for actual_line in input_list:
    actual_line = actual_line.split()
    if actual_line[0] == "$":
        if actual_line[1] == "cd":
            if actual_line[2] == "..":
                if actual_directory[-1][1] < 100000:
                    answer += actual_directory[-1][1]
                actual_directory.pop()
            else:
                actual_directory.append([actual_line[2], 0])
    elif actual_line[0] != "dir":
        for i in actual_directory:
            i[1]+= int(actual_line[0])

print(answer)