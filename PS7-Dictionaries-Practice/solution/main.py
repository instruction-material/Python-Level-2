glossary = {
    "cake": "A baked dessert.",
    "chocolate": "A food made from cacao.",
    "sherbet": "A frozen fruit dessert.",
    "pie": "A filling baked in pastry.",
    "gelatin": "An ingredient that helps liquids set.",
}
print(f"Glossary: {glossary}")


def factorial(number):
    result = 1
    for factor in range(1, number + 1):
        result *= factor
    return result


squares = {}
factorials = {}
for number in range(1, 26):
    squares[number] = number * number
    factorials[number] = factorial(number)
print(f"Squares: {squares}")
print(f"Factorials: {factorials}")

word = input("Word or short phrase: ").lower()
counts = {}
for character in word:
    if character.isalpha():
        counts[character] = counts.get(character, 0) + 1
print(f"Letters: {dict(sorted(counts.items()))}")
