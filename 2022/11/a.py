import math

input_list = open("input.txt", "r")

class Monkey:
    monkeys = []
    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = name
        self.items = items        
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0
        self.__class__.monkeys.append(self)

    def update_items(self, new_item):
        self.items.append(new_item)


for line in input_list:
    line = line.split()
    if line == []:
        exec("m{0} = Monkey({0}, {1}, {2}, {3}, {4}, {5})".format(name, items, operation, test, if_true, if_false))
    else:
        if line[0] == "Monkey":
            name = line[1].replace(":", "")
        elif line[0] == "Starting":
            items = [int(line[_].replace(",", "")) for _ in range(2, len(line))]
        elif line[0] == "Operation:":
            operation = [line[_] for _ in range(3, len(line))]
        elif line[0] == "Test:":
            test = line[-1]
        elif line[0] == "If":
            if line[1] == "true:":
                if_true = line[-1]
            else:
                if_false = line[-1]
exec("m{0} = Monkey({0}, {1}, {2}, {3}, {4}, {5})".format(name, items, operation, test, if_true, if_false))


for round in range(20):
    for monkey in Monkey.monkeys:
        for i in range(len(monkey.items)):
            monkey.inspected += 1
            new_worry_level = ""
            for o in monkey.operation:
                if o == "old":
                    new_worry_level += str(monkey.items[i])
                else:
                    new_worry_level += str(o)
            monkey.items[i] = eval(new_worry_level)
            monkey.items[i] = math.floor(monkey.items[i]/3)
            if monkey.items[i] % monkey.test == 0:
                exec("m{0}.items.append(monkey.items[i])".format(monkey.if_true))
            else:
                exec("m{0}.items.append(monkey.items[i])".format(monkey.if_false))
        monkey.items = []


monkey_business = []
for k in Monkey.monkeys:
    monkey_business.append(k.inspected)
monkey_business = sorted(monkey_business)
print(monkey_business[-1] * monkey_business[-2])