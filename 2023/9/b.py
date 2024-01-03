original_input = open("input.txt", "r").readlines()

output = 0

def extrapolate(numbers):
    is_zeros = True
    for n in numbers:
        if n != 0:
            is_zeros = False
            break
    
    if is_zeros:
        return 0
    else:
        deltas = []
        for x in range(len(numbers) - 1):
            deltas.append(numbers[x + 1] - numbers[x])

        diff = extrapolate(deltas)
        return numbers[0] - diff
    

for n in range(len(original_input)):
    nums = list(map(int, original_input[n].split()))
    output += extrapolate(nums)

print(output)
