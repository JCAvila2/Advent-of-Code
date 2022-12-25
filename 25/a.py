input_list = open("input.txt", "r").readlines()
lines = [line.replace("\n", "") for line in input_list]

max_len = 0

for line in lines:
    if max_len < len(line):
        max_len = len(line)

SNAFU = {"2" : 2, "1" : 1, "0" : 0, "-": -1, "=" : -2}
DECIMAL = {2 : "2", 1 : "1", 0 : "0", -1 : "-", -2 : "="}
answer = ""
base10 = 0
carry = 0

for i in range(max_len):
    sum_i = carry
    for line in lines:
        if i < len(line):
            sum_i += SNAFU[line[len(line) - 1 - i]]
    carry = 0
    while sum_i >= 3:
        carry += 1
        sum_i -= 5
    while sum_i <= -3:
        carry -= 1
        sum_i += 5
    answer += DECIMAL[sum_i]
    base10 += sum_i * 5 ** i

print(answer[::-1])