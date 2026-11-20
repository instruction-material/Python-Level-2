message = input("Sample message: ")
shift = int(input("Shift: "))

for letter in message:
    if "a" <= letter <= "z":
        position = ord(letter) - ord("a")
        print(letter, "shifted position:", position + shift)
    else:
        print(letter)

# Wrap a shifted position with modulo 26 and convert it back to a letter.
# Add the uppercase range and print the assembled result.
