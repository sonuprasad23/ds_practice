letters = ['x','y', 'z']

index_map_loop = {}

for  i in range(len(letters)):
    index_map_loop[letters[i]] = i

print(f"Loop index map : {index_map_loop}")

index_map_comp = {letters[i]: i for i in range (len(letters))}

print(f"Comp index map {index_map_comp}")

assert index_map_loop == index_map_comp

# Comprehension Version (using enumerate)
index_map_enum = {letter: index for index,letter in enumerate(letters)}
print(f"Comp index map(enum): {index_map_enum}")

assert index_map_loop == index_map_enum