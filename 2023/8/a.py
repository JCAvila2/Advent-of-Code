original_input = open("input.txt", "r").readlines()

instructions = original_input[0].replace("\n", "")
nodes = {}
actual_node = "AAA"
actual_instructions = 0
output = 0

for n in range(2, len(original_input)):
    id, moves = original_input[n].replace("\n", "").split(" = ")
    nodes[id] = tuple(moves.replace("(", "").replace(")", "").split(", "))
    
while actual_node != "ZZZ":
    if instructions[actual_instructions] == "L":
        actual_node = nodes[actual_node][0]
    else:
        actual_node = nodes[actual_node][1]

    if actual_instructions == len(instructions) - 1:
        actual_instructions = 0
    else:
        actual_instructions += 1

    output += 1

print(output)
