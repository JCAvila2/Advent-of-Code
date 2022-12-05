input_list = open("input.txt", "r").readlines()

ship = [ 
    ["B", "L", "D", "T", "W", "C", "F", "M"],
    ["N", "B", "L"],
    ["J", "C", "H", "T", "L", "V"],
    ["S", "P", "J", "W"],
    ["Z", "S", "C", "F", "T", "L", "R"],
    ["W", "D", "G", "B", "H", "N", "Z"],
    ["F", "M", "S", "P", "V", "G", "C", "N"],
    ["W", "Q", "R", "J", "F", "V", "C", "Z"],
    ["R", "P", "M", "L", "H"]
]

for order in range(len(input_list)):
    trasfered_items = []
    actual_order = input_list[order].split()
    amount = int(actual_order[1])
    source = int(actual_order[3]) - 1
    destiny = int(actual_order[5]) - 1

    for item in ship[source][::-1]:
        if len(trasfered_items) < amount:
            trasfered_items.append(item)
        else:
            break
    
    for i in trasfered_items:
        ship[source].pop()
        ship[destiny].append(i)

answer = ""
for stacks in ship:
    answer += stacks[-1]
print(answer)