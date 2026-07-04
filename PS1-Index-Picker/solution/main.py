###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

word = input("Enter a word: ")
index = int(input("Enter an index: "))

print("The word you entered was: " + word)
print("The letter at index " + str(index) + " of " + word + " is: " + word[index])
