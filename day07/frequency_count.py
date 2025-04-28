text = "hello world programming"

char_counts={}

for char in text:
    if char ==' ':
        continue

    char_counts[char] =  char_counts.get(char, 0)+1


print(f"Character counts for '{text}': {char_counts}")