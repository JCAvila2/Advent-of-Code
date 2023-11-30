lines = open("input.txt", "r").readlines()

x_register = 1
cicle = 0
grid = [['_' for _ in range(40)] for _ in range(6)]

def update_grid(C, X):
    global grid
    c1 = C - 1
    if abs(X - (c1 % 40)) <= 1:
        grid[c1 // 40][c1 % 40] = "#"
    else:
        grid[c1 // 40][c1 % 40] = " "

for line in lines:
    words = line.split()
    if words[0] == 'noop':
        cicle += 1
        update_grid(cicle, x_register)
    elif words[0] == 'addx':
        cicle += 1
        update_grid(cicle, x_register)
        cicle += 1
        update_grid(cicle, x_register)
        x_register += int(words[1])

for row in range(6):
    print(''.join(grid[row]))