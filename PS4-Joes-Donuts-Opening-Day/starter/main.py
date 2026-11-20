position = int(input("Customer position: "))

if position < 1:
    print("Enter a positive customer position.")
else:
    if position == 1:
        print("Free donuts for a year!")
    # Use one chain for the opening-day tier.
    print("Year-round offer: buy a dozen and get the 13th free.")
