def translate(word):
  new_word = ""

  for i in range (1,len(word)):
    new_word += word[i]

  new_word += word[0] + 'ay'

  return new_word

word = input("Enter a word to translate into Juni Latin: ")
print("The word " + word + " in Juni Latin is " + translate(word))