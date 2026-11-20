import random

RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
NAMES = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
PRACTICE = ("A", "6", "9", "7", "8", "4", "2")


def hand_value(hand):
    total = 0
    for rank in hand:
        if rank == "A":
            total += 1
        elif rank in NAMES:
            total += 10
        else:
            total += int(rank)
    if "A" in hand and total + 10 <= 21:
        total += 10
    return total


def show_hand(label, hand):
    cards = ", ".join(NAMES.get(rank, rank) for rank in hand)
    print(f"{label}: {cards} = {hand_value(hand)}")


def play_round(deck):
    player = [next(deck), next(deck)]
    dealer = [next(deck), next(deck)]
    show_hand("Player", player)
    player_natural = hand_value(player) == 21
    dealer_natural = hand_value(dealer) == 21
    if player_natural or dealer_natural:
        show_hand("Dealer", dealer)
        if player_natural and dealer_natural:
            print("Tie: both start with 21.")
        elif player_natural:
            print("Player wins with a two-card 21.")
        else:
            print("Dealer wins with a two-card 21.")
        return True

    while hand_value(player) < 21:
        action = input("h to hit, s to stay, q to quit: ").strip().lower()
        if action == "q":
            return False
        if action == "s":
            break
        if action == "h":
            player.append(next(deck))
            show_hand("Player", player)
        else:
            print("Choose h, s or q.")

    player_total = hand_value(player)
    if player_total > 21:
        print("Player busts. Dealer wins.")
        return True
    show_hand("Dealer", dealer)
    while hand_value(dealer) < 17:
        dealer.append(next(deck))
        show_hand("Dealer draws", dealer)
    dealer_total = hand_value(dealer)
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
        deck = list(RANKS) * 4
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
