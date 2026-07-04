###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random
import time

input(
    "Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this game, Jack, Queen, and King are each worth 10 and the Ace is worth 1 or 11.\n\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n\nPress Enter to start playing.\n"
)

# the cardNames dicts translates the J, Q, K, A
card_names = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}


# this function prints out a hand with the appropriate names
def print_hand(hand):
    output_hand = []
    for num in hand:
        if num == 1 or num > 10:
            output_hand.append(card_names[num])
        else:
            output_hand.append(num)
    print(output_hand)
    print()


# this function calculates the possible values of each hand (Ace can be 1 or 11)
def calc_hand_values(hand):
    sum = 0
    num_aces = 0
    for num in hand:
        if num == 1:
            num_aces += 1
            sum += 1
        elif num > 10:
            sum += 10
        else:
            sum += num

    # sum currently holds the minimum possible value of the hand. for each Ace in the hand, we should add 10 to the possible values
    values = [sum]
    for i in range(1, num_aces + 1):
        values.append(sum + i * 10)

    return values


# this function calculates the largest possible value of a hand under 21
def get_final_value(hand):
    final_value = 0
    values = sorted(calc_hand_values(hand))
    for num in values:
        if num <= 21:
            final_value = num

    return final_value


while True:
    player_hand = []

    # deal first two cards to player
    for i in range(2):
        player_hand.append(random.randint(1, 13))

    # print out player's cards
    print("Here is your hand: ")
    print_hand(player_hand)

    # use this variable to track when the game should end immediately
    continue_game = True

    # check for blackjack
    if 21 in calc_hand_values(player_hand):
        print("Blackjack! You win! :D")
        continue_game = False

    if continue_game:
        # ask to Hit or Stay
        hit_or_stay = "H"

        while hit_or_stay == "H":
            while True:
                hit_or_stay = input("Type in H to hit or S to stay:")
                if hit_or_stay == "H" or hit_or_stay == "S":
                    break
                else:
                    print("Invalid input.\n")

            # if Hit, add new card and check if busted
            if hit_or_stay == "H":
                player_hand.append(random.randint(1, 13))
                print("Here is your hand: ")
                print_hand(player_hand)

                hand_values = calc_hand_values(player_hand)
                if min(hand_values) > 21:
                    print("You busted! :(\n")
                    continue_game = False
                    break
                elif 21 in hand_values:
                    print("Blackjack! You win! :D")
                    continue_game = False
                    break

        if continue_game:
            print("Dealer's turn!\n")

            # deal first two cards to dealer
            dealer_hand = []
            for i in range(2):
                dealer_hand.append(random.randint(1, 13))

            # print out dealer's cards
            print("Here is the dealer's hand: ")
            print_hand(dealer_hand)

            # the dealer continues to hit until his hand is at least 17
            while True:
                time.sleep(1)  # make game more realistic
                hand_values = calc_hand_values(dealer_hand)
                if min(hand_values) < 17:
                    dealer_hand.append(random.randint(1, 13))
                    print("The dealer hit. Here is the dealer's new hand:")
                    print_hand(dealer_hand)
                elif 21 in hand_values:
                    print("The dealer got blackjack!")
                    break
                elif min(hand_values) > 21:
                    print("The dealer busted! You win! :)")
                    break
                else:
                    print("The dealer has finalized his hand.")
                    # if the game is still going, see whose hand wins
                    time.sleep(1)
                    if get_final_value(player_hand) > get_final_value(dealer_hand):
                        print("You win! :)\n")
                    elif get_final_value(player_hand) < get_final_value(dealer_hand):
                        print("The dealer won. :(\n")
                    else:
                        print("It's a tie!\n")
                    break

    input("Press Enter to play again!\n")
