###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

card = input("Enter a credit card number: ")

sum_digits = 0
for i in range(0, len(card)):
    sum_digits += int(card[i])
print("The sum of the digits is " + str(sum_digits))

sum_digits = 0
for i in range(0, len(card)):
    if i % 2 == 0:
        sum_digits += int(card[i]) * 2
    else:
        sum_digits += int(card[i])
print(
    "The sum of the digits, with every other digit multipled by 2, is "
    + str(sum_digits)
)

if sum_digits % 10 == 0:
    print("Valid card!")
else:
    print("Invalid card!")
