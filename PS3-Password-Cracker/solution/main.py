###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

password = "tavaenryvahwribyv"

# reverse the string
reversed_str = ""
for i in range(len(password) - 1, -1, -1):
    reversed_str += password[i]

# run through all possible keys from a to z and print out what the original password could have been

for key in range(ord("a"), ord("z") + 1):
    guess = ""
    for i in range(0, len(reversed_str)):
        num = ord(reversed_str[i]) - key
        while num < ord("a"):
            num += 26
        guess += chr(num)
    print(guess)
