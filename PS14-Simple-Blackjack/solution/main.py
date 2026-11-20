import random

PRACTICE = (10, 7, 9, 6, 3)


def play_round(deck):
    player = [next(deck), next(deck)]
    dealer = [next(deck), next(deck)]
    print(f"Player: {player} = {sum(player)}")
    while sum(player) < 21:
        action = input("h to hit, s to stay, q to quit: ").strip().lower()
        if action == "q":
            return False
        if action == "s":
            break
        if action == "h":
            player.append(next(deck))
            print(f"Player: {player} = {sum(player)}")
        else:
            print("Choose h, s or q.")

    player_total = sum(player)
    if player_total > 21:
        print("Player busts. Dealer wins.")
        return True

    print(f"Dealer: {dealer} = {sum(dealer)}")
    while sum(dealer) < 17:
        dealer.append(next(deck))
        print(f"Dealer draws: {dealer} = {sum(dealer)}")
    dealer_total = sum(dealer)

    if dealer_total > 21:
        print("Dealer busts. Player wins.")
    elif player_total > dealer_total:
        print("Player wins.")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("Tie.")
    return True


def main():
    while True:
        mode = input("p for practice, Enter to deal, q to quit: ").strip().lower()
        if mode == "q":
            return
        deck = list(range(2, 12)) * 4
        if mode == "p":
            for card in PRACTICE:
                deck.remove(card)
            deck = list(PRACTICE) + deck
        else:
            random.shuffle(deck)
        if not play_round(iter(deck)):
            return


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("Session ended.")
