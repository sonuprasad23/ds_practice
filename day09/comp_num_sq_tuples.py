num_sq_tuples_loop = []
for x in range(5):
    num_sq_tuples_loop.append((x, x*x))
    print(f"Loop tuples: {num_sq_tuples_loop}")

num_sq_tuples_comp = [(x, x*x) for x in range(5)]
print(f"Comp tuples: {num_sq_tuples_comp}")

assert num_sq_tuples_loop == num_sq_tuples_comp

