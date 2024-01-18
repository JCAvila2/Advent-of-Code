original_input = open("input.txt", "r").read().split("\n")

def hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

output = 0
for line in original_input:
    parts = line.split(",")
    for p in parts:
        output += hash(p)

print(output)
