original_input = open("input.txt", "r")
engine_rows = original_input.readlines()
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n"]
output = 0


def checkBorders(row, col, length):
    isValid = False
    for r in range(col, col + length):
        # Check if the number is in the first row
        if row == 0 and col != 0 and col != len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] != "." and engine_rows[row][r - 1] not in NUMBERS:
                isValid = True
            # Check right
            if engine_rows[row][r + 1] != "." and engine_rows[row][r + 1] not in NUMBERS:
                isValid = True
            # Check down
            if engine_rows[row + 1][r] != "." and engine_rows[row + 1][r] not in NUMBERS:
                isValid = True
            # Check down-left
            if engine_rows[row + 1][r - 1] != "." and engine_rows[row + 1][r - 1] not in NUMBERS:
                isValid = True
            # Check down-right
            if engine_rows[row + 1][r + 1] != "." and engine_rows[row + 1][r + 1] not in NUMBERS:
                isValid = True

        # Check if the number is in the last row
        if row == (len(engine_rows) - 1) and col != 0 and col != len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] != "." and engine_rows[row][r - 1] not in NUMBERS:
                isValid = True
            # Check right
            if engine_rows[row][r + 1] != "." and engine_rows[row][r + 1] not in NUMBERS:
                isValid = True
            # Check up
            if engine_rows[row - 1][r] != "." and engine_rows[row - 1][r] not in NUMBERS:
                isValid = True
            # Check up-left
            if engine_rows[row - 1][r - 1] != "." and engine_rows[row - 1][r - 1] not in NUMBERS:
                isValid = True
            # Check up-right
            if engine_rows[row - 1][r + 1] != "." and engine_rows[row - 1][r + 1] not in NUMBERS:
                isValid = True

        # Check if the number is in the first column
        if col == 0 and row != 0 and row != len(engine_rows) - 1:
            # Check up
            if engine_rows[row - 1][r] != "." and engine_rows[row - 1][r] not in NUMBERS:
                isValid = True
            # Check up-right
            if engine_rows[row - 1][r + 1] != "." and engine_rows[row - 1][r + 1] not in NUMBERS:
                isValid = True
            # Check right
            if engine_rows[row][r + 1] != "." and engine_rows[row][r + 1] not in NUMBERS:
                isValid = True
            # Check down
            if engine_rows[row + 1][r] != "." and engine_rows[row + 1][r] not in NUMBERS:
                isValid = True
            # Check down-right
            if engine_rows[row + 1][r + 1] != "." and engine_rows[row + 1][r + 1] not in NUMBERS:
                isValid = True
        
        # Check if the number is in the last column
        if col == len(engine_rows[row]) - 1 and row != 0 and row != len(engine_rows) - 1:
            # Check up
            if engine_rows[row - 1][r] != "." and engine_rows[row - 1][r] not in NUMBERS:
                isValid = True
            # Check up-left
            if engine_rows[row - 1][r - 1] != "." and engine_rows[row - 1][r - 1] not in NUMBERS:
                isValid = True
            # Check left
            if engine_rows[row][r - 1] != "." and engine_rows[row][r - 1] not in NUMBERS:
                isValid = True
            # Check down
            if engine_rows[row + 1][r] != "." and engine_rows[row + 1][r] not in NUMBERS:
                isValid = True
            # Check down-left
            if engine_rows[row + 1][r - 1] != "." and engine_rows[row + 1][r - 1] not in NUMBERS:
                isValid = True


        # Check if the number is in a corner

        # Check if the number is in the top-left corner
        if row == 0 and col == 0:
            # Check right
            if engine_rows[row][r + 1] != "." and engine_rows[row][r + 1] not in NUMBERS:
                isValid = True
            # Check down
            if engine_rows[row + 1][r] != "." and engine_rows[row + 1][r] not in NUMBERS:
                isValid = True
            # Check down-right
            if engine_rows[row + 1][r + 1] != "." and engine_rows[row + 1][r + 1] not in NUMBERS:
                isValid = True

        # Check if the number is in the top-right corner
        if row == 0 and col == len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] != "." and engine_rows[row][r - 1] not in NUMBERS:
                isValid = True
            # Check down
            if engine_rows[row + 1][r] != "." and engine_rows[row + 1][r] not in NUMBERS:
                isValid = True
            # Check down-left
            if engine_rows[row + 1][r - 1] != "." and engine_rows[row + 1][r - 1] not in NUMBERS:
                isValid = True

        # Check if the number is in the bottom-left corner
        if row == len(engine_rows) - 1 and col == 0:
            # Check right
            if engine_rows[row][r + 1] != "." and engine_rows[row][r + 1] not in NUMBERS:
                isValid = True
            # Check up
            if engine_rows[row - 1][r] != "." and engine_rows[row - 1][r] not in NUMBERS:
                isValid = True
            # Check up-right
            if engine_rows[row - 1][r + 1] != "." and engine_rows[row - 1][r + 1] not in NUMBERS:
                isValid = True

        # Check if the number is in the bottom-right corner
        if row == len(engine_rows) - 1 and col == len(engine_rows[row]) - 1:
            # Check left
            if engine_rows[row][r - 1] != "." and engine_rows[row][r - 1] not in NUMBERS:
                isValid = True
            # Check up
            if engine_rows[row - 1][r] != "." and engine_rows[row - 1][r] not in NUMBERS:
                isValid = True
            # Check up-left
            if engine_rows[row - 1][r - 1] != "." and engine_rows[row - 1][r - 1] not in NUMBERS:
                isValid = True
       

        # Check if the number is in the middle
        if row != 0 and row != len(engine_rows) - 1 and col != 0 and col != len(engine_rows[row]) - 1:
            # Check up
            if engine_rows[row - 1][r] != "." and engine_rows[row - 1][r] not in NUMBERS:
                isValid = True
            # Check up-left
            if engine_rows[row - 1][r - 1] != "." and engine_rows[row - 1][r - 1] not in NUMBERS:
                isValid = True
            # Check up-right
            if engine_rows[row - 1][r + 1] != "." and engine_rows[row - 1][r + 1] not in NUMBERS:
                isValid = True
            # Check left
            if engine_rows[row][r - 1] != "." and engine_rows[row][r - 1] not in NUMBERS:
                isValid = True
            # Check right
            if engine_rows[row][r + 1] != "." and engine_rows[row][r + 1] not in NUMBERS:
                isValid = True
            # Check down
            if engine_rows[row + 1][r] != "." and engine_rows[row + 1][r] not in NUMBERS:
                isValid = True
            # Check down-left
            if engine_rows[row + 1][r - 1] != "." and engine_rows[row + 1][r - 1] not in NUMBERS:
                isValid = True
            # Check down-right
            if engine_rows[row + 1][r + 1] != "." and engine_rows[row + 1][r + 1] not in NUMBERS:
                isValid = True

        if isValid:
            break

    return isValid


# Iterate through each row searching for parts (numbers)
for row in range(len(engine_rows)):
    actual_number = ""
    pos = None

    for col in range(len(engine_rows[row])):
        # Check if the row contains a number
        if engine_rows[row][col].isdigit():
            if actual_number == "":
                pos = col
            actual_number += engine_rows[row][col]
        else:
            if actual_number != "":
                if checkBorders(row, pos, len(actual_number)):
                    output += int(actual_number)
                actual_number = ""
                pos = None

    if actual_number != "":
        if checkBorders(row, pos, len(actual_number)):
            output += int(actual_number)
        actual_number = ""
        pos = None

print(output)
# 532428