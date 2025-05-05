text = "Programming Is Fun"

vowels_loop = set()

for char in text:
    lower_char = char.lower()

    if lower_char in 'aeiou':
        vowels_loop.add(lower_char)

print(f"Loop Vowels: {vowels_loop}")

vowels_comp = {char.lower() for char in text if char.lower() in 'aeiou'}

print(f"Comp Vowels: {vowels_comp}")

assert vowels_loop == vowels_comp