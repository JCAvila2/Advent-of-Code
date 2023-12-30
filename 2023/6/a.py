original_input = open("input.txt", "r").readlines()
time_collection, distance_collection = original_input
time_collection = list(map(int, time_collection.replace("Time: ", "").split()))
distance_collection = list(map(int, distance_collection.replace("Distance: ", "").split()))

output = 1

for race in range(len(time_collection)):
    options = 0
    for t in range(1, time_collection[race]):
        distance = t * (time_collection[race] - t)
        if distance > distance_collection[race]:
            options += 1
    output *= options

print(output)
