sentence = input("Sentence for letter counts: ").lower()
letters = set()
for character in sentence:
    if character.isalpha():
        letters.add(character)
print(f"Unique letters: {''.join(sorted(letters))}")
print(f"Unique letter count: {len(letters)}")

paragraph = input("Paragraph for word counts: ").lower()
normalized = ""
for character in paragraph:
    if character.isalpha():
        normalized += character
    else:
        normalized += " "
all_words = normalized.split()
print(f"Unique words: {', '.join(sorted(set(all_words)))}")
print(f"Unique word count: {len(set(all_words))} of {len(all_words)} total")
