original_input = open("input.txt", "r")
list_of_games = original_input.readlines()

LIMITS = {'red' : 12, 'green' : 13, 'blue' : 14}
output = 0

for i in range(len(list_of_games)):
    list_of_games[i] = list_of_games[i].replace("\n", "")
    gameID, record = list_of_games[i].split(":")
    gameID = int(gameID.replace("Game ", ""))
    record = record.split(";")
    isValid = True

    for j in range(len(record)):
        total_per_game = {'red' : 0, 'green' : 0, 'blue' : 0}
        ac_record = record[j].split(',')
        for c in range(len(ac_record)):
            amount, color = ac_record[c][1:].split(" ")
            total_per_game[color] += int(amount)

        for key, value in LIMITS.items():
            if LIMITS[key] < total_per_game[key]:
                isValid = False
                break
        
        if not isValid:
            break

    if isValid:
        output += gameID

print(output)
    