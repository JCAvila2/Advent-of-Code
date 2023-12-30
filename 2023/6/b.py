original_input = open("input.txt", "r").readlines()
time, distance = original_input
time = time.replace("Time: ", "").replace(" ", "")
distance = distance.replace("Distance: ", "").replace(" ", "")

output = 0

for t in range(1, int(time)):
    d = t * (int(time) - t)
    if d > int(distance):
        output += 1
    
print(output)
