original_input = open("input.txt", "r")
list_of_games = original_input.readlines()

output = 0

for i in range(len(list_of_games)):
    list_of_games[i] = list_of_games[i].replace("\n", "")
    gameID, record = list_of_games[i].split(":")
    gameID = int(gameID.replace("Game ", ""))
    record = record.split(";")
    min_per_game = {'red' : 0, 'green' : 0, 'blue' : 0}
    
    for j in range(len(record)):
        ac_record = record[j].split(',')
        for c in range(len(ac_record)):
            amount, color = ac_record[c][1:].split(" ")
            min_per_game[color] = max(min_per_game[color], int(amount))

    output += min_per_game['red'] * min_per_game['green'] * min_per_game['blue']

print(output)
