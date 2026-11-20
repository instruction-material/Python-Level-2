position = int(input("Customer position: "))

if position < 1:
    print("Enter a positive customer position.")
else:
    if position == 1:
        print("Free donuts for a year!")

    if position <= 12:
        print("One dozen free donuts!")
    elif position == 144:
        print("Free donuts for a month!")
    elif position <= 200:
        print("The first dozen costs $1.")
    elif position <= 500:
        print("50% off this purchase!")
    else:
        print("Buy two donuts and get the third free!")

    print("Year-round offer: buy a dozen and get the 13th free.")
