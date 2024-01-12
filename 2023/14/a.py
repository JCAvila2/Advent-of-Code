original_input = open("input.txt", "r").read().strip().split("\n")

n, m = len(original_input), len(original_input[0])
output = 0

for col in range(m):
    ans = 0
    i = 0

    while i < n:
        while i < n and original_input[i][col] == "#":
            i += 1
        
        start = i
        count = 0
        while i < n and original_input[i][col] != "#": 
            if original_input[i][col] == "O":
                count += 1
            i += 1

        for j in range(start, start + count):
            ans += n - j

    output += ans

print(output)
