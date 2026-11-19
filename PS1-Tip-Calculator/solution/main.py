bill = float(input("Bill amount in dollars: "))
tip_rate = float(input("Tip rate as a decimal, such as 0.18: "))

tip = bill * tip_rate
total = bill + tip

print(f"Whole-dollar tip estimate, rounded down: ${int(tip)}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
