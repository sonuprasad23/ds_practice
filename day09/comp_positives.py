nums = [-2, -1, 0, 1, 2, 3]

positive_loop = []

for x in nums:
    if x>0:
        positive_loop.append(x)
        print(f"Loop positives: {positive_loop}")

positives_comp = [x for x in nums if x>0]
print(f"Comp positives: {positives_comp}")
assert positive_loop ==positives_comp


