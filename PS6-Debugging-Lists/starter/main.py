# Repair the syntax error first. Then check how the list changes after input.
flavors = flavor[]

for index in range(5):
    suggestion = input(f"Flavor {index + 1}: ").strip().lower()
    flavors = flavors + suggestion

for flavor in flavors:
    print(flavors[index])

chocolate_count = 0
pistachio_count = 0
for flavor in range(flavors):
    if flavor == "chocolate mudslide":
        chocolate_count += 1
    elif flavor == "pistachio":
        pistachio_count += 1

print(f"Chocolate mudslide: {chocolate_count}")
print(f"Pistachio: {pistachio_count}")
