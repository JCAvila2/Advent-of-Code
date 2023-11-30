input_list = open("input.txt", "r").readlines()

answer = 0
for row in range(len(input_list)):
    for column in range(len(input_list[row]) - 1):
        if row >= 1 and column >= 1 and column < len(input_list[row]) - 2 and row < len(input_list) - 1:
            
            if int(input_list[row][column]) > int(input_list[row - 1][column]):
                k = True
                for r in range(row - 1, -1, -1):
                    if int(input_list[row][column]) <= int(input_list[r][column]):
                        k = False
                        break
                if k:
                    answer += 1
                    continue

            if int(input_list[row][column]) > int(input_list[row + 1][column]):
                k = True
                for r in range(row + 1, len(input_list)):
                    if int(input_list[row][column]) <= int(input_list[r][column]):
                        k = False
                        break
                if k:
                    answer += 1
                    continue

            if int(input_list[row][column]) > int(input_list[row][column - 1]):
                k = True
                for c in range(column - 1, -1, -1):
                    if int(input_list[row][column]) <= int(input_list[row][c]):
                        k = False
                        break
                if k:
                    answer += 1
                    continue

            if int(input_list[row][column]) > int(input_list[row][column + 1]):
                k = True
                for c in range(column + 1, len(input_list)):
                    if int(input_list[row][column]) <= int(input_list[row][c]):
                        k = False
                        break
                if k:
                    answer += 1

print(answer + (len(input_list[0]) - 1) * 2 + (len(input_list) - 2) * 2)