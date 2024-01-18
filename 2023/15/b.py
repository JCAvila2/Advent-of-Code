original_input = open("input.txt", "r").read().split("\n")

def hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

output = 0
boxes = [[] for b in range(256)]
focal_lenght = {}

for line in original_input:
    instructions = line.split(",")
    for i in instructions:
        if "=" in i:
            operation, length = i.split("=")
            index = hash(operation)
            length = int(length)
            if operation not in boxes[index]:
                boxes[index].append(operation)
            focal_lenght[operation] = length
        else:
            operation = i[:-1]
            index = hash(operation)
            if operation in boxes[index]:
                boxes[index].remove(operation)

for number, box in enumerate(boxes, 1):
    for lens, label in enumerate(box, 1):
        output += lens * focal_lenght[label] * number

print(output)
