text = input("Enter a short line: ")
offset = ord("a") - ord("A")
converted = ""

for letter in text:
    code = ord(letter)
    if ord("A") <= code <= ord("Z"):
        code += offset
    converted += chr(code)

print("Converted:", converted)
