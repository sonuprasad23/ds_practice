# day12/stdlib_random_choices.py
import random

my_list = ['A', 'B', 'C', 'D', 'E']
print(f"Original list: {my_list}")

print(f"Random choice: {random.choice(my_list)}")
# choices allows for replacement by default, so could get same element twice
print(f"Random 2 choices (with replacement): {random.choices(my_list, k=2)}")
# sample ensures unique elements
print(f"Random 2 samples (unique): {random.sample(my_list, k=2)}")

random.shuffle(my_list) # Shuffles in-place
print(f"Shuffled list: {my_list}")