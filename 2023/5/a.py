import sys

original_input = open("input.txt", "r").readlines()
seeds = original_input[0].replace("seeds: ", "").split(" ")
instructions = {}
output = sys.maxsize

for line in range(2, len(original_input)):
    if original_input[line] == "\n":
        actual_step = ""
    elif original_input[line][0].isdigit():
        instructions[actual_step].append(original_input[line].replace("\n", ""))
    else:
        actual_step = original_input[line].replace(":", "").replace("\n", "").replace(" map", "")
        instructions[actual_step] = []

for s in seeds:
    next_category_number = int(s)
    for k, v in instructions.items():
        for range in v:
            destination_range_start, source_range_start, range_length = range.split(" ")
            source_range_end = int(source_range_start) + int(range_length) - 1
            if next_category_number >= int(source_range_start) and next_category_number <= source_range_end:
                next_category_number = int(destination_range_start) + (int(next_category_number) - int(source_range_start))
                break
    output = min(output, next_category_number)
        
print(output)
