from functools import cmp_to_key

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


packets = []
packets.append([[2]])
packets.append([[6]])
list1 = None
list2 = None
for line in input_list:
    if line == "\n":
        list1 = None
        list2 = None
    else:
        if list1 == None:
            exec("list1 = {0}".format(line))
        else:
            exec("list2 = {0}".format(line))
            packets.append(list1)
            packets.append(list2)

packets = sorted(packets, key = cmp_to_key(lambda item1, item2: right_order(item1, item2)))
for l in packets:
    if l == [[2]]:
        pos1 = packets.index(l) + 1
    elif l ==[[6]]:
        pos2 = packets.index(l) + 1
print(pos1 * pos2)