d_orig = {'a':1, 'b':3, 'c':1, 'd':3, 'e':2}

d_inverted={}

for key, value in d_orig.items():

    key_list=d_inverted.setdefault(value,[])

    key_list.append(key)

print(f"Originak dictionary: {d_orig}")
print(f"Inverted dictionary: {d_inverted}")