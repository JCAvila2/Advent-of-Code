import copy

original_input = open("input.txt", "r")
list_of_elf_calories = copy.deepcopy(original_input.readlines())
output = []
actual_elf_calories = 0

for product in range(len(list_of_elf_calories)):
    if list_of_elf_calories[product] == "\n":
        output.append(actual_elf_calories)
        actual_elf_calories = 0
    else:
        actual_elf_calories += int(list_of_elf_calories[product])

output_sorted = sorted(output)
print("Sorted output:", output_sorted)
print("b):", output_sorted[len(output_sorted)-1] + output_sorted[len(output_sorted)-2] + output_sorted[len(output_sorted)-3])