sentence = "comprehensions are cool"

vowels_comp = {char for char in sentence if char in "aeiou"}
print(f"Vowels found in sentence{vowels_comp}")


# Netsted List Comprehension
matrix = [[1,2], [3,4], [5,6]]
flattened = [element for row in matrix for element in row]
print("Original matrix:", matrix)
print("Flattened matrix:", flattened)

# List comp conditional
nums = range(10)
result = [x if x%2==0 else "odd" for x in nums]
print(f"Conditional list:{result}")