import re


positive_words = {
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
}

negative_words = {
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
}


def classify_review(review):
    words = re.findall(r"[a-z]+", review.lower())
    if not words:
        print("No words to score.")
        return

    positive = sum(word in positive_words for word in words)
    negative = sum(word in negative_words for word in words)
    print(f"Positive: {positive}/{len(words)} ({positive / len(words):.1%})")
    print(f"Negative: {negative}/{len(words)} ({negative / len(words):.1%})")
    if positive > negative:
        print("Sentiment: positive")
    elif negative > positive:
        print("Sentiment: negative")
    else:
        print("Sentiment: neutral")


try:
    review = input("Enter a short English review: ")
except EOFError:
    review = ""
classify_review(review)
