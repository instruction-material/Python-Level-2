###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random
import time

input(
    "Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this simple version of Blackjack, we only use the cards 2 through 11 (Ace).\n\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n\nPress Enter to start playing.\n"
)

while True:
    player_hand = []

    # deal first two cards to player
    for i in range(2):
        player_hand.append(random.randint(2, 11))

    # print out player's cards
    print("Here is your hand: ")
    print(player_hand)

    # use this variable to track when the game should end immediately
    continue_game = True

    # check for blackjack
    if sum(player_hand) == 21:
        print("Blackjack! You win! :D")
        continue_game = False

    if continue_game:
        # ask to Hit or Stay
        hit_or_stay = "H"
        continue_game = True  # use this variable to track whether the game ends immediately after this
        while hit_or_stay == "H":
            while True:
                hit_or_stay = input("Type in H to hit or S to stay:")
                if hit_or_stay == "H" or hit_or_stay == "S":
                    break
                else:
                    print("Invalid input.\n")

            # if Hit, add new card and check if busted
            if hit_or_stay == "H":
                player_hand.append(random.randint(2, 11))
                print("Here is your hand: ")
                print(player_hand)

                if sum(player_hand) > 21:
                    print("You busted! :(\n")
                    continue_game = False
                    break
                elif sum(player_hand) == 21:
                    print("Blackjack! You win! :D")
                    continue_game = False
                    break

        if continue_game:
            print("Dealer's turn!\n")

            # deal first two cards to dealer
            dealer_hand = []
            for i in range(2):
                dealer_hand.append(random.randint(2, 11))

            # print out dealer's cards
            print("Here is the dealer's hand: ")
            print(dealer_hand)

            # the dealer continues to hit until his hand is at least 17
            while True:
                time.sleep(1)  # make game more realistic
                if sum(dealer_hand) < 17:
                    dealer_hand.append(random.randint(2, 11))
                    print("The dealer hit. Here is the dealer's new hand:")
                    print(dealer_hand)
                elif sum(dealer_hand) == 21:
                    print("The dealer got blackjack!")
                    break
                elif sum(dealer_hand) > 21:
                    print("The dealer busted! You win! :)")
                    break
                else:
                    print("The dealer has finalized his hand.")
                    # if the game is still going, see whose hand wins
                    time.sleep(1)
                    if sum(player_hand) > sum(dealer_hand):
                        print("You win! :)\n")
                    elif sum(player_hand) < sum(dealer_hand):
                        print("The dealer won. :(\n")
                    else:
                        print("It's a tie!\n")
                    break

    input("Press Enter to play again!\n")
