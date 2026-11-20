flavors = []
for index in range(5):
    suggestion = input(f"Flavor {index + 1}: ").strip().lower()
    flavors.append(suggestion)

chocolate_count = 0
pistachio_count = 0
for flavor in flavors:
    print(flavor)
    if flavor == "chocolate mudslide":
        chocolate_count += 1
    elif flavor == "pistachio":
        pistachio_count += 1

print(f"Chocolate mudslide: {chocolate_count}")
print(f"Pistachio: {pistachio_count}")
