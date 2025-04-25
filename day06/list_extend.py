list1=[1,2]
list2=[3,4]
list1_copy=list1.copy()


print(f"List1 before extending: {list1}")
list1.extend(list2)
print(f"List 1 after extend(list2):{list1}")

print(f"List1_copy before append: {list1_copy}")
list1_copy.append(list2)
print(f"List1_copy after append(list2): {list1_copy}")

