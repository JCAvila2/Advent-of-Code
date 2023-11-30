import copy

input_list = open("input.txt", "r").readlines()

sensor_x = None
sensor_y = None
sensors = set()
beacon_x = None
beacon_y = None
beacons = set()
no_beacons = set()
y = 2000000


def make_r(sensor, distance):
    global no_beacons, y
    y_up = sensor[1]
    k = copy.deepcopy(distance)
    while y_up != sensor[1] - distance - 1:
        if y_up == y:
            for i in range(k + 1):   
                no_beacons.add((sensor[0] + i, y_up))
                no_beacons.add((sensor[0] - i, y_up))
        y_up -= 1
        k -= 1
    y_down = sensor[1]
    k = copy.deepcopy(distance)
    while y_down != sensor[1] + distance + 1:
        if y_down == y:
            for i in range(k + 1):    
                no_beacons.add((sensor[0] + i, y_down))
                no_beacons.add((sensor[0] - i, y_down))
        y_down += 1
        k -= 1


for line in input_list:
    line = line.split()
    exec("sensor_" + line[2].replace(",", ""))
    exec("sensor_" + line[3].replace(":", ""))
    sensors.add((sensor_x, sensor_y))
    exec("beacon_" + line[8].replace(",", ""))
    exec("beacon_" + line[9].replace("\n", ""))
    beacons.add((beacon_x, beacon_y))
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    make_r((sensor_x, sensor_y), distance)

print(len(no_beacons) - 1)