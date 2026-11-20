candies = {
    "Caramel": 15,
    "Almond chocolate": 7,
    "Wafer bar": 6,
    "Crisp bar": 9,
    "Peanut cup": 3,
    "Toffee": 2,
}

print(f"Original total: {sum(candies.values())}")
for candy in candies:
    candies[candy] = max(0, candies[candy] - 1)

candies["Wafer bar"] = 0
candies["Mint"] = candies.get("Mint", 0) + 4
for candy, count in candies.items():
    print(f"{candy}: {count}")
print(f"Final total: {sum(candies.values())}")
