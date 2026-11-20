def is_even(number):
    return number % 2 == 0


print("Even numbers:")
for number in range(1, 51):
    if is_even(number):
        print(number)

# Add the other predicates and reuse the existing helper where possible.
