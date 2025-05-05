words = ["py", "list", "dict", "set", "comprehension"]

long_lengths_loop = []

for w in words:
    if len(w)>3:
        long_lengths_loop.append(len(w))
        print(f"Loop long Lengths: {long_lengths_loop}")

long_lengths_comp = [len(w) for w in words if len(w)>3]
print(f"Comp long lengths: {long_lengths_comp}")

assert long_lengths_loop == long_lengths_comp

