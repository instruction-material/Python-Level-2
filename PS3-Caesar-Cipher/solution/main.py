def shift_ascii(message, shift):
    result = ""
    for letter in message:
        if "a" <= letter <= "z":
            base = ord("a")
        elif "A" <= letter <= "Z":
            base = ord("A")
        else:
            result += letter
            continue

        position = ord(letter) - base
        wrapped = (position + shift) % 26
        result += chr(base + wrapped)
    return result


message = input("Sample message: ")
shift = int(input("Shift: "))
shifted = shift_ascii(message, shift)
print("Shifted:", shifted)
print("Restored:", shift_ascii(shifted, -shift))
