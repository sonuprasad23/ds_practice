from mymath import add, PI ,subtract

result_add_direct = add(100, 50) 
pi_direct = PI                   
print(f"\nUsing 'from mymath import add, PI':")
print(f"  add(100, 50) = {result_add_direct}")
print(f"  PI = {pi_direct}")

try:
    result_sub_direct = subtract(10, 3)
    print(f"  subtract(10, 3) = {result_sub_direct}")
except NameError as e:
    print(f"  Error calling subtract(): {e}")