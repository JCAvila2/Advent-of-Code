input_list = open("input.txt", "r").readlines()

total_counter = 0

for section in input_list:
    first_elf, second_elf = section.split(",")
    first_elf = first_elf.split("-")
    second_elf = second_elf.split("-")

    if int(first_elf[0]) < int(second_elf[0]) and int(first_elf[1]) > int(second_elf[1]):
        total_counter += 1
    elif int(second_elf[0]) < int(first_elf[0]) and int(first_elf[1]) < int(second_elf[1]):
        total_counter += 1
    elif int(first_elf[0]) in range(int(second_elf[0]), int(second_elf[1]) + 1) or int(first_elf[1]) in range(int(second_elf[0]), int(second_elf[1]) + 1):
        total_counter += 1
    elif int(second_elf[0]) in range(int(first_elf[0]), int(first_elf[1]) + 1) or int(second_elf[1]) in range(int(first_elf[0]), int(first_elf[1]) + 1):
        total_counter += 1

print(total_counter)