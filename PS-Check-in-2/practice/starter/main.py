sentence = input("Sentence for letter counts: ")
letters = set()
for character in sentence.lower():
    if character.isalpha():
        letters.add(character)
print(f"Unique letter count: {len(letters)}")

# Ask for a paragraph. Count every word and build a set of unique words.
