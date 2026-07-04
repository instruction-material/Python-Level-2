import pysynth

# Reminder for using psynth:
# 1) You can see the project files by clicking the file icon on the sidebar to the left!
# 2) Do not click on the wav file until the program is finished running (i.e. once you see the blue Run button again instead of the red Stop button)

morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

# 1. Define a function that takes in a message and converts that message into morse code. (Make sure to put extra spaces inbetween your words.) Using the function, ask the user for a message and print out the translated message.

def translate_to_morse_code(msg):
  morse_msg = ""
  for letter in msg:
    if letter == " ":
      morse_msg += "  "
    else:
      morse_msg += morse_dict[letter] + " "
  return morse_msg

msg = input("Type in a message to translate into morse code (in all lowercase): ")
print(translate_to_morse_code(msg))

# 2. Define a function that takes in a message and converts that message into musical morse code. Each dot should be a C for an eighth note, and each dash should be a C for a half note. Rest for a half note inbetween each word and an eighth note between each dot or dash.

def translate_to_morse_code_music(msg):
  song = []
  for letter in msg:
    if letter == " ":
      song.append(('r', 2))
    else:
      morse_char = morse_dict[letter]
      for char in morse_char:
        if char == ".":
          song.append(('c', 8))
        elif char == "-":
          song.append(('c', 2))
        song.append(('r', 8))

  return song

msg = input("Type in a message to translate into morse code music (in all lowercase): ")
pysynth.make_wav(translate_to_morse_code_music(msg), fn="morseSong.wav")