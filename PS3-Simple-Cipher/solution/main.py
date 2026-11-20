message = input("Sample message: ")
offset = int(input("Numeric offset: "))
original = ""
shifted = ""

for letter in message:
    code = ord(letter)
    original += str(code) + " "
    shifted += str(code + offset) + " "

print("Original codes:", original.rstrip())
print("Shifted codes:", shifted.rstrip())
