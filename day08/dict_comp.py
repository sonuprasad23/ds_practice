words = ["data", "science", "rocks"]

word_lengths = {word: len(word) for word in words}

print(f"Word lengths dictionary: {word_lengths}")


# Invert dictionary

d_orig = {'a':1, 'b':2, 'c':3}

d_inverted = {value: key for key, value in d_orig.items()}
print(f"Original :{d_orig}")
print(f"Inverted :{d_inverted}")

# Dict comp filter

prices = {"apple":0.5, "banana":0.25, "orange": 0.6, "grape":1.5}   
expensive_fruits = {fruit: price for fruit, price in prices.items() if price > 0.5}

print(f"Expensive fruits(>$0.50): {expensive_fruits}")

# Unique squares
unique_squares = {x**2 for x in range(-3,4)}
print(f"Unique squares(-3 to 3): {unique_squares}")

# Unique first letter

wordss = ["apple", "banana", "apricot", "blueberry", "cherry"]
first_letters = {word[0] for word in wordss if word}
print(f"Unique first letters: {first_letters}")
