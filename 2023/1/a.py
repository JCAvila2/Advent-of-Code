import copy

original_input = open("input.txt", "r")
list_of_values = copy.deepcopy(original_input.readlines())

numbers = ["1","2","3","4","5","6","7","8","9","0"]
output = 0


for word in list_of_values:

    first_number = None
    for c in word:
        if c in numbers:
            first_number = c
            break
    last_number = None
    for c in range(len(word) -1, -1, -1):
        if word[c] in numbers:
            last_number = word[c]
            break

    total = first_number + last_number
    output += int(total)

print(output)