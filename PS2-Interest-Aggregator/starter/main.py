balance = float(input("Starting balance: "))
annual_percent = float(input("Annual rate as a percent: "))
annual_rate = annual_percent / 100

balance *= 1 + annual_rate
print(f"Year 1: {balance:.2f}")

# Replace the single update with a loop that projects all 20 years.
