balance = float(input("Starting balance: "))
annual_percent = float(input("Annual rate as a percent: "))
annual_rate = annual_percent / 100

print(f"Starting balance: {balance:.2f}")
for year in range(1, 21):
    balance *= 1 + annual_rate
    print(f"Year {year}: {balance:.2f}")
