def add_one(n):
    return n+1

nums = [1,2,3,4]

plus_one_iterator = map(add_one, nums)

plus_one_list = list(plus_one_iterator)

print(f"List after map(add_one): {plus_one_list}")
