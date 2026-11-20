word = input("One word: ").strip()
if word.isalpha():
    print(f"First character: {word[0]}")
    # Move this logic into a function and assemble the translated word.
else:
    print("Enter one word made of letters.")
