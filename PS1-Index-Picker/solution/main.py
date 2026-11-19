word = input("Enter a word or phrase: ")
print("Word:", word)

try:
    index = int(input("Enter an index: "))
except ValueError:
    print("Enter a whole-number index.")
else:
    if 0 <= index < len(word):
        print(f"Character at index {index}: {word[index]}")
    else:
        print("That index is outside the word.")
