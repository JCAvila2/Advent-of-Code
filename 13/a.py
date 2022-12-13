input_list = open("input.txt", "r").readlines()


def right_order(item1, item2):
    if type(item1) == int and type(item2) == int:
        if item1 < item2:
            return -1
        elif item1 == item2:
            return 0
        else:
            return 1
    elif type(item1) == list and type(item2) == list:
        i = 0
        while i < len(item1) and i < len(item2):
            recursive = right_order(item1[i], item2[i])
            if recursive == -1:
                return -1
            if recursive == 1:
                return 1
            i += 1
        if i == len(item1) and i < len(item2):
            return -1
        elif i < len(item1) and i == len(item2):
            return 1    
        else: 
            return 0
    elif type(item1) == int and type(item2) == list:
        return right_order([item1], item2)
    else:
        return right_order(item1, [item2])


answer = 0
list1 = None
list2 = None
actual_pair = 1
for line in input_list:
    if line == "\n":
        actual_pair += 1
        list1 = None
        list2 = None 
    else:
        if list1 == None:
            exec("list1 = {0}".format(line))
        else:
            exec("list2 = {0}".format(line))
            if right_order(list1, list2) == -1:
                answer += actual_pair 
            
print( answer)