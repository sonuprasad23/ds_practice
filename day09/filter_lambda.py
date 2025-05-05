nums = range(10)

odd_iterator = filter(lambda x: x % 2 != 0, nums)

print(f"Filter Object: {odd_iterator}")

odd_list = list(odd_iterator)
print(f"List of odds fro filter: {odd_list}")