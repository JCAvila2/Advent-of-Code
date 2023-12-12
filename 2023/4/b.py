original_input = open("input.txt", "r")
list_of_cards = original_input.readlines()

amount_of_each = {}

for game in list_of_cards:
    game = game.replace("\n", "")
    card_number = game.split(":")[0]
    Winning_numbers, numbers = game.split(":")[1].split("|")
    Winning_numbers = Winning_numbers.split(" ")
    Winning_numbers = [int(n) for i,n in enumerate(Winning_numbers) if n != ""]
    numbers = numbers.split(" ")
    numbers = [int(n) for i,n in enumerate(numbers) if n != ""]
    ID = int("".join(c for c in card_number if c.isdecimal()))
    
    if ID not in amount_of_each.keys():
        amount_of_each[ID] = 1

    card_score = 0
    for number in numbers:
        if number in Winning_numbers:
            card_score += 1

    for number in range(ID + 1, ID + card_score + 1):
        amount_of_each[number] = amount_of_each.get(number, 1) + amount_of_each[ID]


print(sum(amount_of_each.values()))
