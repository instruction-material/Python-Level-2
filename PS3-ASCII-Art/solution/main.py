###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

size = int(input("Enter the size of the box: "))

for i in range(size):
    for j in range(size):
        print("#", end="")
    print()
