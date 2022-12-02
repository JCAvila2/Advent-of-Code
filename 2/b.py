import copy

original_input = open("input.txt", "r")
list_of_matches = copy.deepcopy(original_input.readlines())
total_score = 0
for match in range(len(list_of_matches)):
    if list_of_matches[match][0] == "A":
        if list_of_matches[match][2] == "X":
            total_score += 0+3
        if list_of_matches[match][2] == "Y":
            total_score += 3+1
        if list_of_matches[match][2] == "Z":
            total_score += 6+2
    elif list_of_matches[match][0] == "B":
        if list_of_matches[match][2] == "X":
            total_score += 0+1
        if list_of_matches[match][2] == "Y":
            total_score += 3+2
        if list_of_matches[match][2] == "Z":
            total_score += 6+3
    elif list_of_matches[match][0] == "C":
        if list_of_matches[match][2] == "X":
            total_score += 0+2
        if list_of_matches[match][2] == "Y":
            total_score += 3+3
        if list_of_matches[match][2] == "Z":
            total_score += 6+1

print(total_score)