def is_long_word(word):
    """Return True if word length is greater than 5"""
    return len(word) > 5


words = ["python", "is", "awesome", "and", "powerful"]

long_words_iterator = filter(is_long_word, words)
long_words_list = list(long_words_iterator)

print(f"List of long words from filter: {long_words_list}")