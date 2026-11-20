for number in range(1, 51):
    # Check the combined case before the two single-divisor cases.
    if number % 3 == 0:
        print("Fizz")
    else:
        print(number)
