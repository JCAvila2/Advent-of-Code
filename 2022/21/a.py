input_list = open("input.txt", "r").readlines()


monkeys_completed = {}
monkeys_incompleted = {}
waiting_list = []

for line in input_list:
    line = line.split()
    name = line[0].replace(":", "")
    
    try:
        monkeys_completed[name] = int(line[1])
    except:
        first_monkey = line[1]
        second_monkey = line[3]
        operation = line[2]
        if first_monkey in monkeys_completed.keys() and second_monkey in monkeys_completed.keys():
            monkeys_completed[name] = int(eval(str(monkeys_completed[first_monkey]) + operation + str(monkeys_completed[second_monkey])))
        else:
            monkeys_incompleted[name] = [first_monkey, operation, second_monkey]
            waiting_list.append(name)
            
    m = 0
    while m < len(waiting_list):
        first_monkey, operation, second_monkey = monkeys_incompleted[waiting_list[m]]
        if first_monkey in monkeys_completed.keys() and second_monkey in monkeys_completed.keys():
            monkeys_completed[waiting_list[m]] = int(eval(str(monkeys_completed[first_monkey]) + operation + str(monkeys_completed[second_monkey])))            
            del monkeys_incompleted[waiting_list[m]]
            waiting_list.pop(m)
            m = 0
            continue
        else:
            m += 1
    
print(monkeys_completed["root"])