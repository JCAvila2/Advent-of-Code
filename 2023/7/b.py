original_input = open("input.txt", "r").readlines()

P = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hands = []

def getType(hand):
    repetitions = {}
    for i in hand:
        if i in repetitions:
            repetitions[i] += 1
        else:
            repetitions[i] = 1

    amounts_sorted = sorted(repetitions.values(), reverse=True)

    if len(amounts_sorted) == 5:
        return 0
    elif amounts_sorted == [2, 1, 1, 1]:
        return 1
    elif amounts_sorted == [2, 2, 1]:
        return 2
    elif amounts_sorted == [3, 1, 1]:
        return 3
    elif amounts_sorted == [3, 2]:
        return 4
    elif amounts_sorted == [4, 1]:
        return 5
    elif len(amounts_sorted) == 1:
        return 6


for line in original_input:
    line = line.replace("\n", "")
    hand, bid = line.split()

    if "J" not in hand:
        hands.append([getType(hand), hand, int(bid)])
    else:
        strongest_option = getType(hand)
        for i in range(len(P) - 1):
            option = getType(hand.replace("J", P[i]))
            if strongest_option < option:
                strongest_option = option
        hands.append([strongest_option, hand, int(bid)])
    
hands = sorted(hands, key=lambda x: x[0])


for i in range(len(hands) - 1):
    if hands[i][0] != hands[i + 1][0]:
        continue
    for j in range(i + 1, len(hands)):
        if hands[i][0] != hands[j][0]:
            break
        for k in range(5):
            if P.index(hands[i][1][k]) < P.index(hands[j][1][k]):
                hands[i], hands[j] = hands[j], hands[i]
                break
            elif P.index(hands[i][1][k]) > P.index(hands[j][1][k]):
                break
            
output = 0
for h in range(len(hands)):
    output += hands[h][2] * (h + 1)

print(output)
