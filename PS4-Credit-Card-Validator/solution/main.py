sample = input("Fictional digit string: ").strip()

if len(sample) < 2 or not sample.isascii() or not sample.isdigit():
    print("Enter at least two ASCII digits.")
else:
    total = 0
    double_digit = False
    for character in sample[::-1]:
        digit = int(character)
        if double_digit:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        double_digit = not double_digit

    print(f"Checksum total: {total}")
    if total % 10 == 0:
        print("Checksum passes.")
    else:
        print("Checksum fails.")
