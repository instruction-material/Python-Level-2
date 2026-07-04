###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# Part 1: Ask the user for a secret message. Then, print out the message translated into ASCII, with a space between each character.
msg = input("Type in your message to encrypt: ")
new_msg = ""

for i in range(0, len(msg)):
    num = ord(msg[i])
    new_msg += str(num) + " "

print(new_msg)

# Part 2: Now, we will make the cipher more difficult. This time, ask for another secret message, but print out the message translated into ASCII, with a constant number (a key) added to each number. This is the secret key the recipient would use to decode your message.

msg = input("Type in your message to encrypt: ")
key = int(input("Type in the key you wish to use: "))
new_msg = ""
for i in range(0, len(msg)):
    num = ord(msg[i])
    new_msg += str(num + key) + " "

print(new_msg)
