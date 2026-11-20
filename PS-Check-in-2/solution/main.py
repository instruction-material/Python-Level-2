import random


def multiply(left, right):
    return left * right


def lottery_result(won, amount):
    if won:
        return f"The lottery prize is {amount} dollars."
    return "No lottery prize."


print(f"15 times 22: {multiply(15, 22)}")
print(lottery_result(random.randint(0, 1), random.randint(1, 1000)))

guests = []
guests.append("Ava")
guests.append("Ben")
guests.append("Mina")
print(f"Starting guests: {guests}")
guests.remove("Ava")
print(f"First remaining guest: {guests[0]}")
print("Final guest list:")
for guest in guests:
    print(guest)

numbers = []
evens = []
for number in range(1, 21):
    numbers.append(number)
    if number % 2 == 0:
        evens.append(number)
print(f"Numbers: {numbers}")
print(f"Evens: {evens}")

jerseys = {"Parker": 3, "Reed": 11, "Rivera": 7}
print(f"Reed: {jerseys['Reed']}")
jerseys["Diaz"] = 10
if "Curry" not in jerseys:
    jerseys["Curry"] = 30
for player in jerseys:
    print(f"{player}: {jerseys[player]}")

digit_counts = {}
for number in random.sample(range(1001), 15):
    digit_counts[number] = len(str(number))
print(f"Digit counts: {digit_counts}")

recipe = {"garlic", "onion", "salt"}
recipe.remove("onion")
second_recipe = {"apple", "cinnamon", "salt"}
shared_ingredients = recipe.intersection(second_recipe)
all_ingredients = recipe.union(second_recipe)
print(f"All ingredients: {', '.join(sorted(all_ingredients))}")
print(f"Shared ingredients: {', '.join(sorted(shared_ingredients))}")
if "garlic" in shared_ingredients:
    print("Garlic is in both recipes.")
elif "garlic" in all_ingredients:
    print("Garlic is in one recipe.")
else:
    print("Garlic is in neither recipe.")
print(f"Different letters in banana: {len(set('banana'))}")
