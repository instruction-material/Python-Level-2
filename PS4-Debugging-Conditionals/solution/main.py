###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

num_tickets = int(input("How many tickets did you win? "))

lollipop_price = 10
action_figure_price = 75
tshirt_price = 250
stuffed_animal_price = 350

# Print out which items you can afford, and how many tickets you'd have left if you bought it
if (
    num_tickets < lollipop_price
    and num_tickets < action_figure_price
    and num_tickets < tshirt_price
    and num_tickets < stuffed_animal_price
):
    print("You can't afford anything by yourself")
if num_tickets >= lollipop_price:
    print(
        "You can buy a lollipop, but you'll only have "
        + str(num_tickets - lollipop_price)
        + " tickets left"
    )
if num_tickets >= action_figure_price:
    print(
        "You can buy an action figure, but you'll only have "
        + str(num_tickets - action_figure_price)
        + " tickets left"
    )
if num_tickets >= tshirt_price:
    print(
        "You can buy a t-shirt, but you'll only have "
        + str(num_tickets - tshirt_price)
        + " tickets left"
    )
if num_tickets >= stuffed_animal_price:
    print(
        "You can buy a stuffed animal, but you'll only have "
        + str(num_tickets - stuffed_animal_price)
        + " tickets left"
    )

# You and Kant want to buy matching t-shirts, but he is short 6 tickets. Can you afford to loan him 6 tickets and still buy a t-shirt yourself?
# If you can't afford to get two t-shirts, can you afford to get just one? (remember Kant already has 244 tickets)
if num_tickets >= tshirt_price + 6:
    print("You can get matching t-shirts!")
elif num_tickets >= tshirt_price:
    print(
        "Sorry, you can't get matching t-shirts, but you can afford a single t-shirt!"
    )
