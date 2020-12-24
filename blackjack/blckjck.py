import random
dealer_cards = []
player_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("У диллера две карты")

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("У тебя", player_cards)


while sum(player_cards) < 21:
    action_taken = str(input("Еще?\n"))
    if action_taken == "Да":
        player_cards.append(random.randint(1, 11))
        print("На руках у тебя " + str(sum(player_cards)) + " из ", player_cards)
    else:
        print("У диллера " + str(sum(dealer_cards)) + " из ", dealer_cards)
        print("У тебя " + str(sum(player_cards)) + " из ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Диллер выиграл!")
            break
        else:
            print("Ты выиграл!")
            break

if sum(dealer_cards) == 21:
    print("У диллера блэкджек. Он победил")
elif sum(dealer_cards) > 21:
    print("У диллера перебор. Он проиграл")

if sum(player_cards) > 21:
    print("У тебя перебор, диллер выиграл")
elif sum(player_cards) == 21:
    print("У тебя блэкджек, ты выиграл")
