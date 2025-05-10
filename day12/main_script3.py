import mymath as mm 

result_add_aliased = mm.add(7, 2)
pi_aliased = mm.PI

print(f"\nUsing 'import mymath as mm':")
print(f"  mm.add(7, 2) = {result_add_aliased}")
print(f"  mm.PI = {pi_aliased}")