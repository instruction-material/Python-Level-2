###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# Create a list to store the flavors
flavors = []

# Ask my 5 best friends for ice cream recommendations
for i in range(5):
    suggestion = input(
        "Friend " + str(i + 1) + ", what kind of ice cream should I get? "
    )
    flavors.append(suggestion)


# Print out all of the suggestions
print("\nMy friends' suggestions:")
for flavor in flavors:
    print(flavor)


# Check if any of my friends recommended chocolate mudslide (my favorite flavor) or pistachio (my least favorite flavor)
num_chocolate_mudslide = 0
num_pistachio = 0
for i in range(len(flavors)):
    if flavors[i] == "chocolate mudslide":
        num_chocolate_mudslide += 1
    elif flavors[i] == "pistachio":
        num_pistachio += 1

print()
print(
    str(num_chocolate_mudslide)
    + " of my friends wanted chocolate mudslide, one of my favorite flavors!"
)
print(str(num_pistachio) + " of my friends wanted pistachio, my least favorite flavor!")
