msg = input("Type in your message to encrypt: ")
key = int(input("Type in the key you wish to use: "))
new_msg = ''

for i in range(0,len(msg)):
  num = ord(msg[i]) + key
  while num > ord('z'):
    num -= 26
  new_msg += chr(num)

print(new_msg)

msg = input("Type in your message to decrypt: ")
key = int(input("Type in the decryption key: "))
new_msg = ''

for i in range(0,len(msg)):
  num = ord(msg[i]) - key
  while num < ord('a'):
    num += 26
  new_msg += chr(num)

print(new_msg)