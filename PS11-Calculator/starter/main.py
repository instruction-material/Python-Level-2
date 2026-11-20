def add(left, right):
    return left + right


left = int(input("First whole number: "))
right = int(input("Second whole number: "))
print(f"{left} + {right} = {add(left, right)}")

# Add the operation menu and the remaining arithmetic helpers.
# Ask again after invalid input, or exit when the user enters q.
