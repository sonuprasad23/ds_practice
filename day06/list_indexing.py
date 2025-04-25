n_list=[1,2,3,4,5]

print(f"FIrst element: {n_list[0]}")
print(f"Third element: {n_list[2]}")
print(f"Last elemeent: {n_list[-1]}")

try:
    print(f"Element at index 10 : {m_list[10]}")

except IndexError:
    print("Error: Index 10 is out of bounds for n_list.")