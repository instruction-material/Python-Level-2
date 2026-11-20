message = "Eoxh frphw!"
shift = 3
decoded = ""
for letter in message:
    if "a" <= letter <= "z":
        decoded += chr(ord("a") + (ord(letter) - ord("a") - shift) % 26)
    elif "A" <= letter <= "Z":
        decoded += chr(ord("A") + (ord(letter) - ord("A") - shift) % 26)
    else:
        decoded += letter
print(f"Shift {shift}: {decoded}")

# Put the decoding into a function and print every numbered candidate.
