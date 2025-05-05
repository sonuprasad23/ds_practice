nums = [1, 2, 3, 4]

squares_iterator = map(lambda x:x*x, nums)

print(f"Map Object: {squares_iterator}")

squares_list = list(squares_iterator)

print(f"List of squares from map: {squares_list}")