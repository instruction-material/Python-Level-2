# Repair the dictionary literal before running the other checks.
candies = {
    "Caramel" 15,
    "Almond chocolate": 7,
    "Wafer bar": 6,
    "Crisp bar": 9,
    "Peanut cup": 3,
    "Toffee": 2,
}

for candy in candies:
    print(f"{candy}: {candies[index]}")

for candy in candies:
    candy = candy - 1

candies["Wafer bar"] = 0
candies["Mint"] = candies["Mint"] + 4

for candy in candies:
    print(f"{candy}: {candies[candy]}")
print(f"Final total: {sum(candies.values())}")
