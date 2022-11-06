cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
hand_player = [random.choice(cards)]
hand_computer = [random.choice(cards)]
score_player = 0
score_computer = 0
get_card = "y"
while get_card == "y":
    hand_player.append(random.choice(cards))

    if sum(hand_player) > 21 and 11 in hand_player:
        for i in range(0,len(hand_player)):
            if hand_player[i] == 11:
                hand_player[i] = 1

    score_player = sum(hand_player)
    print(f"твоя рука: {hand_player}. очков: {score_player}")
    print("первая карта компутера:", hand_computer[0])
    if score_player > 21:
        get_card = "n"
    else:
        get_card = input("y - взять карту, n - остановится")

    while sum (hand_computer) < 17:
        hand_computer.append(random.choice(cards))
        if sum(hand_player) > 21 and 11 in hand_player:
            for i in range(0, len(hand_player)):
                if hand_player[i] == 11:
                    hand_player[i] = 1
    score_computer = sum(hand_computer)
    print("=" * 10)
    print(f"твоя итоговоя рука: {hand_player}.очков: {score_player}")
    print(f"итоговоя рука компутера: {hand_computer}.очков: {score_computer}")

    if score_computer > 21 and score_player > 21:
        print("перелёт у обоих. Ничья.")
    elif score_player > score_computer:
        print("перебор компютера. выйграл.")
    elif score_player <  21:
        print(")

