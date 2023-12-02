import copy

original_input = open("input.txt", "r")
list_of_values = copy.deepcopy(original_input.readlines())

numbers_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
output = 0


for word in list_of_values:

    found = {}

    for key, value in numbers_dict.items():
        # first number
        first_number_in_letters = word.find(value)
        if first_number_in_letters != -1:
            found[first_number_in_letters] = value

        # last number
        last_number_in_letters = word.rfind(value)
        if last_number_in_letters != -1:
            found[last_number_in_letters] = value


        # first letter
        first_number_str = word.find(key)
        if first_number_str != -1:
            found[first_number_str] = value

        # last letter
        last_number_str = word.rfind(key)
        if last_number_str != -1:
            found[last_number_str] = value


    first = min(found.keys())
    last = max(found.keys())

    total = found[first] + found[last]
    output += int(total)

print(output)