set1= set()

set2= {1,2,2,3,4,4,4}

list_for_set=[1,2,2,3,4,4,4]

set2_from_list= set(list_for_set)

set3= {"a", "b", "c"}

print(f"Empty set: {set1}")
print(f"Set from literals: {set2}")
print(f"Set from list: {set2_from_list}")
print(f"Set of strings: {set3}")

wrong_empty = {}
print(f"Incorrect empty set: {wrong_empty}, Type: {type(wrong_empty)}")