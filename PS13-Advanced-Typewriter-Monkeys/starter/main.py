with open("valid_words.txt", encoding="utf-8") as file:
    words = {line.strip() for line in file if len(line.strip()) == 3}

window = ""
for count, letter in enumerate("xcatmint", start=1):
    window = (window + letter)[-3:]
    if len(window) == 3:
        print(f"Window: {window}")
        if window in words:
            print(f"Found {window} after {count} letters.")
            break

# Read a target length, filter its words, and add a bounded random stream.
