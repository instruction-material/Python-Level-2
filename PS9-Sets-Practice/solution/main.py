import random


def letters(text):
    result = set()
    for character in text.lower():
        if character.isalpha():
            result.add(character)
    return result


def get_evens(numbers):
    result = set()
    for number in numbers:
        if number % 2 == 0:
            result.add(number)
    return result


def get_three_letter_words(words):
    result = set()
    for word in words:
        if len(word) == 3:
            result.add(word)
    return result


first = set(random.sample(range(1, 11), 5))
second = set(random.sample(range(1, 11), 5))
print(f"First set: {sorted(first)}")
print(f"Second set: {sorted(second)}")
print(f"Union: {sorted(first.union(second))}")
print(f"Intersection: {sorted(first.intersection(second))}")
print(f"Second set includes 1: {1 in second}")

first_letters = letters(input("First word: "))
second_letters = letters(input("Second word: "))
print(f"Unique first letters: {', '.join(sorted(first_letters)) or 'none'}")
print(f"Unique first letter count: {len(first_letters)}")
print(f"Shared letters: {', '.join(sorted(first_letters & second_letters)) or 'none'}")
print(f"Even numbers: {sorted(get_evens({1, 2, 3, 4}))}")
print(f"Three-letter words: {', '.join(sorted(get_three_letter_words({'cat', 'bat', 'house'})))}")
