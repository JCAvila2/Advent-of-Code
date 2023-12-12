original_input = open("input.txt", "r")
list_of_cards = original_input.readlines()

output = 0

for game in list_of_cards:
    game = game.replace("\n", "")
    Winning_numbers, numbers = game.split(":")[1].split("|")
    Winning_numbers = Winning_numbers.split(" ")
    Winning_numbers = [int(n) for i, n in enumerate(Winning_numbers) if n != ""]
    numbers = numbers.split(" ")
    numbers = [int(n) for i,n in enumerate(numbers) if n != ""]

    card_value = 0
    for number in numbers:
        if number in Winning_numbers:
            if card_value == 0:
                card_value = 1
            else:
                card_value *= 2

    output += card_value

print(output)
