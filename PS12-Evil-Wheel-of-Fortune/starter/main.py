with open("dictionary.txt", encoding="utf-8") as source:
    words = set(source.read().split())

sample = {word for word in words if len(word) == 3}
print(f"Three-letter candidates: {len(sample)}")
