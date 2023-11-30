input_list = open("input.txt", "r").readlines()

priority_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
total_priority = 0

for element in input_list:
    first_half = []
    second_half = []
    position = 0
    for item in element:
        position += 1
        if position <= len(element)//2:
            first_half.append(item)
        else:
            second_half.append(item)

    for item in first_half:
        if item in second_half:
            if str(item).islower():
                addition = priority_dict.get(str(item))
                total_priority += addition
            else:
                addition = priority_dict.get(str(item).lower())
                total_priority += addition + 26
            break
    
print(total_priority)