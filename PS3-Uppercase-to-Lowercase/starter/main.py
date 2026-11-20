text = input("Enter a short line: ")
offset = ord("a") - ord("A")

for letter in text:
    print(letter, ord(letter))

# When a code is between ord("A") and ord("Z"), add offset.
# Assemble the changed and unchanged characters into one output.
