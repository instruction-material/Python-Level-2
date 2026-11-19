remaining = int(input("Amount in cents: "))
quarters = 0

while remaining >= 25:
    remaining -= 25
    quarters += 1

print("Quarters:", quarters)
print("Remaining cents:", remaining)

# Add counters for dimes, nickels, and pennies using the same remaining value.
