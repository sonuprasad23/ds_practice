squares = [x**2 for x in range(10)]
print(f"Squares (0-9): {squares}")

#Even nummbers from 1 -19
evens = [x for x in range(20) if x%2==0]
print(f"Even numbers (0-19): {evens}")

#Upper case for fruits
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {upper_fruits}")

#Loop to list
words = ["hello", "world", "python", "is", "fun"]

lengths_comp = [len(word) for word in words]
print(f"Length of words: {lengths_comp}")

# Loops to lists
numbers = [1 ,5, 10, 15, 20, 25]
results_comp = [num//10 for num in numbers if num %10==0]
print(f "Results (divisible by 10, then divided): {results_comp}")  