dup_list = [1,'a', 2, 'b', 1, 'a', 'c', 3]
print(f"Original list with duplicates: {dup_list}")

unique_set = set(dup_list)
print(f"Set with unique elements: {unique_set}")

unique_list = list(unique_set)
print(f"List with unique elements(order not gauranteed): {unique_list}")