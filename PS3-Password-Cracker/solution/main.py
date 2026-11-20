def decode(message, shift):
    decoded = ""
    for letter in message:
        if "a" <= letter <= "z":
            first = ord("a")
        elif "A" <= letter <= "Z":
            first = ord("A")
        else:
            decoded += letter
            continue
        index = (ord(letter) - first - shift) % 26
        decoded += chr(first + index)
    return decoded


sample = "Eoxh frphw!"
for shift in range(26):
    print(f"Shift {shift}: {decode(sample, shift)}")
