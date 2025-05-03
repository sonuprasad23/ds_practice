squares_lc = [x**2 for x in range(10)]
print(f"List comp types: {type(squares_lc), Value: {squares_lc}}")

squares_gen = (x**2 for x in range(10))
print(f"Gen Expr Type: {squares_gen}, Value: {squares_gen}")

print(f"\nIterating through generator expression:")
for square in squares_gen:
    print(square)

print(f"\nTrying to iterate again: (iterator exhausted)")

for square in squares_gen:
    print(square)


    