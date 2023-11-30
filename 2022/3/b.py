input_list = open("input.txt", "r").readlines()

total_priority = 0

priority_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
group = []

for element in input_list:
    if len(group) == 2:
        group.append(element)
        for item in group[0]:    
            if item in group[1] and item in group[2]:
                if str(item).islower():
                    addition = priority_dict.get(str(item))
                    total_priority += addition
                else:
                    addition = priority_dict.get(str(item).lower())
                    total_priority += addition + 26
                break
        group.clear()
    else:
        group.append(element)
        
print(total_priority)