s_a = {1,2,3}
s_b = {3,4,5}
print(f"Set A {s_a}")
print(f"Set B: {s_b}")

sym_diff_method = s_a.symmetric_difference(s_b)
print(f"Symmetric diffference method : {sym_diff_method}")

sym_diff_operator = s_a ^ s_b
print(f"Symmertic difference operator: {sym_diff_operator}")