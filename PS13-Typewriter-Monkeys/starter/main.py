with open("valid_words.txt", encoding="utf-8") as source:
    valid_words = set(source.read().split())

print(f"Loaded {len(valid_words)} three-letter words.")
