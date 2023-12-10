original_input = open("input.txt", "r")
engine_rows = original_input.readlines()

output = 0
engine_parts = {}
gears = {}

def checkGears(row, col, length):
    pos = None
    isValid = False

    for r in range(col, col + length):
        # Check if the number is in the first row
        if row == 0 and col != 0 and col != len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] == "*":
                isValid = True
                pos = (row, r - 1)
            # Check right
            if engine_rows[row][r + 1] == "*":
                isValid = True
                pos = (row, r + 1)
            # Check down
            if engine_rows[row + 1][r] == "*":
                isValid = True
                pos = (row + 1, r)
            # Check down-left
            if engine_rows[row + 1][r - 1] == "*":
                isValid = True
                pos = (row + 1, r - 1)
            # Check down-right
            if engine_rows[row + 1][r + 1] == "*":
                isValid = True
                pos = (row + 1, r + 1)

        # Check if the number is in the last row
        if row == (len(engine_rows) - 1) and col != 0 and col != len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] == "*":
                isValid = True
                pos = (row, r - 1)
            # Check right
            if engine_rows[row][r + 1] == "*":
                isValid = True
                pos = (row, r + 1)
            # Check up
            if engine_rows[row - 1][r] == "*":
                isValid = True
                pos = (row - 1, r)
            # Check up-left
            if engine_rows[row - 1][r - 1] == "*":
                isValid = True
                pos = (row - 1, r - 1)
            # Check up-right
            if engine_rows[row - 1][r + 1] == "*":
                isValid = True
                pos = (row - 1, r + 1)

        # Check if the number is in the first column
        if col == 0 and row != 0 and row != len(engine_rows) - 1:
            # Check up
            if engine_rows[row - 1][r] == "*":
                isValid = True
                pos = (row - 1, r)
            # Check up-right
            if engine_rows[row - 1][r + 1] == "*":
                isValid = True
                pos = (row - 1, r + 1)
            # Check right
            if engine_rows[row][r + 1] == "*":
                isValid = True
                pos = (row, r + 1)
            # Check down
            if engine_rows[row + 1][r] == "*":
                isValid = True
                pos = (row + 1, r)
            # Check down-right
            if engine_rows[row + 1][r + 1] == "*":
                isValid = True
                pos = (row + 1, r + 1)
        
        # Check if the number is in the last column
        if col == len(engine_rows[row]) - 1 and row != 0 and row != len(engine_rows) - 1:
            # Check up
            if engine_rows[row - 1][r] == "*":
                isValid = True
                pos = (row - 1, r)
            # Check up-left
            if engine_rows[row - 1][r - 1] == "*":
                isValid = True
                pos = (row - 1, r - 1)
            # Check left
            if engine_rows[row][r - 1] == "*":
                isValid = True
                pos = (row, r - 1)
            # Check down
            if engine_rows[row + 1][r] == "*":
                isValid = True
                pos = (row + 1, r)
            # Check down-left
            if engine_rows[row + 1][r - 1] == "*":
                isValid = True
                pos = (row + 1, r - 1)


        # Check if the number is in a corner

        # Check if the number is in the top-left corner
        if row == 0 and col == 0:
            # Check right
            if engine_rows[row][r + 1] == "*":
                isValid = True
                pos = (row, r + 1)
            # Check down
            if engine_rows[row + 1][r] == "*":
                isValid = True
                pos = (row + 1, r)
            # Check down-right
            if engine_rows[row + 1][r + 1] == "*":
                isValid = True
                pos = (row + 1, r + 1)

        # Check if the number is in the top-right corner
        if row == 0 and col == len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] == "*":
                isValid = True
                pos = (row, r - 1)
            # Check down
            if engine_rows[row + 1][r] == "*":
                isValid = True
                pos = (row + 1, r)
            # Check down-left
            if engine_rows[row + 1][r - 1] == "*":
                isValid = True
                pos = (row + 1, r - 1)

        # Check if the number is in the bottom-left corner
        if row == len(engine_rows) - 1 and col == 0:
            # Check right
            if engine_rows[row][r + 1] == "*":
                isValid = True
                pos = (row, r + 1)
            # Check up
            if engine_rows[row - 1][r] == "*":
                isValid = True
                pos = (row - 1, r)
            # Check up-right
            if engine_rows[row - 1][r + 1] == "*":
                isValid = True
                pos = (row - 1, r + 1)

        # Check if the number is in the bottom-right corner
        if row == len(engine_rows) - 1 and col == len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] == "*":
                isValid = True
                pos = (row, r - 1)
            # Check up
            if engine_rows[row - 1][r] == "*":
                isValid = True
                pos = (row - 1, r)
            # Check up-left
            if engine_rows[row - 1][r - 1] == "*":
                isValid = True
                pos = (row - 1, r - 1)
       

        # Check if the number is in the middle
        if row != 0 and row != len(engine_rows) - 1 and col != 0 and col != len(engine_rows[row]) - 1:
            # Check up
            if engine_rows[row - 1][r] == "*":
                isValid = True
                pos = (row - 1, r)
            # Check up-left
            if engine_rows[row - 1][r - 1] == "*":
                isValid = True
                pos = (row - 1, r - 1)
            # Check up-right
            if engine_rows[row - 1][r + 1] == "*":
                isValid = True
                pos = (row - 1, r + 1)
            # Check left
            if engine_rows[row][r - 1] == "*":
                isValid = True
                pos = (row, r - 1)
            # Check right
            if engine_rows[row][r + 1] == "*":
                isValid = True
                pos = (row, r + 1)
            # Check down
            if engine_rows[row + 1][r] == "*":
                isValid = True
                pos = (row + 1, r)
            # Check down-left
            if engine_rows[row + 1][r - 1] == "*":
                isValid = True
                pos = (row + 1, r - 1)
            # Check down-right
            if engine_rows[row + 1][r + 1] == "*":
                isValid = True
                pos = (row + 1, r + 1)

        if isValid:
            break

    return isValid, pos


for row in range(len(engine_rows)):
    actual_number = ""
    pos = None
    for col in range(len(engine_rows[row])):
        if engine_rows[row][col].isdigit():
            if actual_number == "":
                pos = col
            actual_number += engine_rows[row][col]
        else:
            if engine_rows[row][col] == "*":
                gears[(row, col)] = []
            if actual_number != "":
                valid, gpos = checkGears(row, pos, len(actual_number))
                if valid:
                    engine_parts[((row, pos), len(actual_number))] = (int(actual_number), gpos)
                actual_number = ""
                pos = None

    if actual_number != "":
        valid, gpos = checkGears(row, pos, len(actual_number))
        if valid:
            engine_parts[((row, pos), len(actual_number))] = (int(actual_number), gpos)
        actual_number = ""
        pos = None

for key, value in engine_parts.items():
    t = gears[value[1]]
    t.append(value[0])
    gears[value[1]] = t

for key, value in gears.items():
    if len(value) == 2:
        res = value[0] * value[1]
        output += res

print(output)
