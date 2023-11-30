input_list = open("input.txt", "r").readlines()

answer = 0
for row in range(len(input_list)):
    for column in range(len(input_list[row])):
        total_view_distance = 0
        if row >= 1 and column >= 1 and column < len(input_list[row]) - 2 and row < len(input_list) - 1:

            counter = 0
            for r in range(row - 1, -1, -1):
                counter += 1
                if int(input_list[row][column]) <= int(input_list[r][column]):
                    break
            total_view_distance += counter

            counter = 0
            for r in range(row + 1, len(input_list)):
                counter += 1
                if int(input_list[row][column]) <= int(input_list[r][column]):
                    break
            total_view_distance *= counter

            counter = 0
            for c in range(column - 1, -1, -1):
                counter += 1
                if int(input_list[row][column]) <= int(input_list[row][c]):
                    break
            total_view_distance *= counter

            counter = 0
            for c in range(column + 1, len(input_list)):
                counter += 1
                if int(input_list[row][column]) <= int(input_list[row][c]):
                    break
            total_view_distance *= counter

        if total_view_distance > answer:
            answer = total_view_distance

print(answer)