height = int(input("Height in inches: "))
print(f"Height: {height} inches")

if height < 50:
    print("No prize.")
elif height < 100:
    print("Small stuffed animal.")
elif height < 150:
    print("Frisbee.")
else:
    print("Large stuffed animal.")
