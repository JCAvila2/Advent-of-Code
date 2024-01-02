from math import gcd

original_input = open("input.txt", "r").readlines()

instructions = original_input[0].replace("\n", "")
nodes = {}
list_of_nodes = []
cycles = []


for n in range(2, len(original_input)):
    id, moves = original_input[n].replace("\n", "").split(" = ")
    nodes[id] = tuple(moves.replace("(", "").replace(")", "").split(", "))
    

for n in nodes:
    if n[2] == "A":
        list_of_nodes.append(n)


for current in list_of_nodes:
    cycle = []
    current_steps = instructions
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = nodes[current][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]

        cycle.append(step_count)
        
        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break
    
    cycles.append(cycle)


nums = []
for cycle in cycles:
    nums.append(cycle[0])


lcm = nums.pop()
for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)
