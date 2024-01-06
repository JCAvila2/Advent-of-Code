original_input = open("input.txt", "r").read().strip().split("\n")


def count_options(signs, records):
    if signs == "":
        return 1 if records == () else 0
    
    if records == ():
        return 0 if "#" in signs else 1

    res = 0
    if signs[0] in ".?":
        res += count_options(signs[1:], records)

    if signs[0] in "#?":
        if records[0] <= len(signs) and "." not in signs[:records[0]] and (records[0] == len(signs) or signs[records[0]] != "#"):
            res += count_options(signs[records[0] + 1:], records[1:])
        
    return res
    

output = 0
for line in original_input:
    signs, records = line.split(" ")
    records = tuple(map(int, records.split(",")))
    count = count_options(signs, records)
    output += count

print(output)
