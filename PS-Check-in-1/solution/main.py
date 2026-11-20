word = "animal"
number = 42
number_text = str(number)
print(f"Stored word: {word}")
print(f"42 converted to text: {number_text}")

animal = input("Animal: ").strip().lower()
color = input("Color: ").strip().lower()
print(f"Animal length: {len(animal)}")
if len(color) >= 3:
    print(f"Third color character: {color[2]}")
else:
    print("No third color character.")
print(f"Guess: {color} {animal}")

print("For loop from 0 to 10:")
for number in range(11):
    print(number)

print("Color characters:")
for character in color:
    print(character)

print("Every third number from 6 to 15:")
for number in range(6, 16, 3):
    print(number)

print("While loop from 0 to 15:")
counter = 0
while counter < 16:
    print(counter)
    counter += 1

print("Every other animal character from index 1:")
index = 1
while index < len(animal):
    print(animal[index])
    index += 2

if animal == "cat":
    print("Cat guess recorded.")

if animal == "dog" and color == "black":
    print("Correct answer!")
elif animal == "dog" or color == "black":
    print("Almost there!")
else:
    print("Incorrect answer.")

print("Nested version:")
if animal == "dog":
    if color == "black":
        print("Correct answer!")
    else:
        print("Almost there!")
elif color == "black":
    print("Almost there!")
else:
    print("Incorrect answer.")

print("Bonus loop from 1 to 10:")
counter = 1
while True:
    print(counter)
    counter += 1
    if counter == 11:
        break
