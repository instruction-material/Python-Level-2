import random
import string

with open("valid_words.txt", encoding="utf-8") as source:
    valid_words = set(source.read().split())

print(f"Loaded {len(valid_words)} three-letter words.")


window = ""
for count in range(1, 10_001):
    window = (window + random.choice(string.ascii_lowercase))[-3:]
    if window in valid_words:
        print(f"Found {window} after {count} generated letters.")
        break
else:
    print("No word found in 10000 generated letters.")
