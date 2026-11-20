message = input("Sample message: ")
codes = ""

for letter in message:
    codes += str(ord(letter)) + " "

print("Original codes:", codes.rstrip())

# Read an integer offset and print the shifted codes for the same message.
