remaining = int(input("Amount in cents: "))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while remaining >= 25:
    remaining -= 25
    quarters += 1
while remaining >= 10:
    remaining -= 10
    dimes += 1
while remaining >= 5:
    remaining -= 5
    nickels += 1
while remaining >= 1:
    remaining -= 1
    pennies += 1

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
print("Remaining cents:", remaining)
