from collections import deque

input_list = open("input.txt", "r").readlines()

list_of_numbers = []
for line in input_list:
    list_of_numbers.append(int(line) * 811589153)

list_of_numbers = deque(list(enumerate(list_of_numbers)))

for mix in range(10):
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if list_of_numbers[j][0] == i:
                break

        while list_of_numbers[0][0] != i:
            list_of_numbers.append(list_of_numbers.popleft())
        val = list_of_numbers.popleft()
        to_pop = val[1]
        to_pop %= len(list_of_numbers)

        for _ in range(to_pop):
            list_of_numbers.append(list_of_numbers.popleft())
        list_of_numbers.append(val)

for j in range(len(list_of_numbers)):
    if list_of_numbers[j][1] == 0:
        break

coordinate_1 = list_of_numbers[(j + 1000) % len(list_of_numbers)][1]
coordinate_2 = list_of_numbers[(j + 2000) % len(list_of_numbers)][1]
coordinate_3 = list_of_numbers[(j + 3000) % len(list_of_numbers)][1]
print(coordinate_1 + coordinate_2 + coordinate_3)