pos_words = [
    "good",
    "great",
    "excellent",
    "awesome",
    "beautiful",
    "amazing",
    "glad",
    "joy",
    "happy",
    "positive",
    "cool",
]

neg_words = [
    "bad",
    "mediocre",
    "poor",
    "lousy",
    "sad",
    "unacceptable",
    "awful",
    "negative",
    "inferior",
    "lame",
    "disappointing",
]

review = input("Enter your review here: ")

words = review.split()
num_pos_words = 0
num_neg_words = 0

for word in words:
    if word in pos_words:
        num_pos_words += 1
    elif word in neg_words:
        num_neg_words += 1

num_words_total = len(words)
perc_pos = (num_pos_words / num_words_total) * 100
perc_neg = (num_neg_words / num_words_total) * 100

print(
    "The review has "
    + str(perc_pos)
    + " percent positive words and "
    + str(perc_neg)
    + " percent negative words."
)

if perc_pos > perc_neg:
    print("I've detected that this review is mostly positive!")
elif perc_neg > perc_pos:
    print("I've detected that this review is mostly negative!")
else:
    print("This review seems to be neutral!")
