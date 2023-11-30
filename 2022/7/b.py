input_list = open("input.txt", "r").readlines()

actual_directory = []
directories = {}

for actual_line in input_list:
    actual_line = actual_line.split()
    if actual_line[0] == "$":
        if actual_line[1] == "cd":
            if actual_line[2] == "..":
                actual_directory.pop()
            else:
                actual_directory.append([actual_line[2], 0])
                if actual_line[2] not in directories.keys():
                    directories[actual_directory[-1][0]] = 0
    elif actual_line[0] == "dir":
        if actual_line[1] not in directories.keys():
            directories[actual_line[1]] = 0
    else:
        for i in actual_directory:
            i[1] += int(actual_line[0])
            directories[i[0]] += int(actual_line[0])

unused_space = 70000000 - max(directories.values())
best_option = max(directories.values())
for size in directories.values():
    if size + unused_space >= 30000000:
        if size < best_option:
            best_option = size
            
print(best_option)