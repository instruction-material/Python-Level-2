###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

dogs = ["beagle", "collie", "greyhound", "komondor", "mastiff", "pug", "terrier"]

for dog in dogs:
    first_letter = dog[0]
    num_letters = str(len(dog))
    print(
        "A "
        + dog
        + " is a dog breed. Its name starts with the letter "
        + first_letter
        + ", and its name has "
        + num_letters
        + " letters in it.\n"
    )
