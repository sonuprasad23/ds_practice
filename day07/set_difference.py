s_a= {1,2,3}
s_b= {3,4,5}

print(f"Set A: {s_a}")
print(f"Set B: {s_b}")

diff_a_b_method = s_a.difference(s_b)
print(f"Difference A-B (method): {diff_a_b_method}")

diff_a_b_operator = s_a - s_b
print(f"Difference A-B operator -: {diff_a_b_operator}")

diff_b_a_method = s_b.difference(s_a)
print(f"Difference B-A (method): {diff_b_a_method}")

diff_b_a_operator = s_b - s_a
print(f"Difference B-A (method): {diff_b_a_operator}")