def translate(word):
    if not word.isalpha():
        return ""
    return word[1:] + word[0] + "ay"


word = input("One word: ").strip()
translation = translate(word)
if translation:
    print(f"{word} becomes {translation}.")
else:
    print("Enter one word made of letters.")
