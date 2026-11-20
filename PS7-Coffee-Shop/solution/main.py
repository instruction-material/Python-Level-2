drinks = [
    "Coffee",
    "Decaf",
    "Vanilla Latte",
    "Mocha",
    "Hot Chocolate",
    "Iced Coffee",
    "Smoothie",
]
prices = [2.50, 2.50, 4.00, 4.25, 3.00, 2.75, 5.25]


def build_menu(names, costs):
    if len(names) != len(costs):
        raise ValueError("Give each item one price.")
    if len(set(names)) != len(names):
        raise ValueError("Use each item name once.")
    return dict(zip(names, costs))


menu = build_menu(drinks, prices)
for drink, cost in menu.items():
    print(f"{drink}: ${cost:.2f}")
