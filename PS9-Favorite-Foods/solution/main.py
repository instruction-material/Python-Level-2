def read_foods(group):
    foods = set()
    for index in range(1, 6):
        food = input(f"{group} food {index} of 5: ").strip().lower()
        while not food:
            food = input("Enter a food name: ").strip().lower()
        foods.add(food)
    return foods


group_a = read_foods("Group A")
group_b = read_foods("Group B")
shared = group_a.intersection(group_b)
only_a = group_a.difference(group_b)
only_b = group_b.difference(group_a)
print(f"Shared: {', '.join(sorted(shared)) or 'none'}")
print(f"Only Group A: {', '.join(sorted(only_a)) or 'none'}")
print(f"Only Group B: {', '.join(sorted(only_b)) or 'none'}")
