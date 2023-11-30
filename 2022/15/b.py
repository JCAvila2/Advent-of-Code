input_list = open("input.txt", "r").readlines()


sensor_x = None
sensor_y = None
beacon_x = None
beacon_y = None
grid = []


for line in input_list:
    line = line.split()
    exec("sensor_" + line[2].replace(",", ""))
    exec("sensor_" + line[3].replace(":", ""))
    exec("beacon_" + line[8].replace(",", ""))
    exec("beacon_" + line[9].replace("\n", ""))
    grid.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))


for y in range(0, 4000000):
    free_xs = []
    for sensor, beacon in grid:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        distance_y = abs(sensor[1] - y)
        if distance_y <= distance:
            distance_x = distance - distance_y
            free_xs.append((max(sensor[0] - distance_x, 0), min(sensor[0] + distance_x, 4000000)))
    free_xs = sorted(free_xs)
    combined_distances = [free_xs[0]]
    for dis in free_xs[1:]:
        if dis[0] > combined_distances[-1][1]:
            combined_distances.append(dis)
        else:
            combined_distances[-1] = (combined_distances[-1][0], max([combined_distances[-1][1], dis[1]]))
    if len(combined_distances) > 1 or (combined_distances[0][0] > 0 and combined_distances[0][1] > 4000000):
        if len(combined_distances) == 1:
            if combined_distances[0][0] > 0:
                x = 0
            else:
                x = 4000000
        else:
            x = combined_distances[0][1] + 1
        break

print(x * 4000000 + y)