# Extra practice. This helper applies the same alphabet rule in both loops.
def shift_letter(character, change):
    if "A" <= character <= "Z":
        start = ord("A")
    elif "a" <= character <= "z":
        start = ord("a")
    else:
        return character
    return chr(start + (ord(character) - start + change) % 26)


length_sample = input("Text for the length rule: ")
length_shift = 1 if len(length_sample) % 2 == 0 else -1
shifted_by_length = ""
for character in length_sample:
    shifted_by_length += shift_letter(character, length_shift)
print(f"Length rule: {shifted_by_length}")

index_sample = input("Text for the index rule: ")
shifted_by_index = ""
for index in range(len(index_sample)):
    index_shift = 1 if index % 2 == 0 else -1
    shifted_by_index += shift_letter(index_sample[index], index_shift)
print(f"Index rule: {shifted_by_index}")
