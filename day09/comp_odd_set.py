nums = [ 1,2,3,4,5,6,7,7,8]

odd_set_loop = []

odd_set_loop = set()

for x in nums:
    if x%2!=0:
        odd_set_loop.add(x)

        print(f"loop odd set: {odd_set_loop}")

odd_set_comp = {x for x in nums if x%2!=0}

print(f"Comp odd set: {odd_set_comp}")

assert odd_set_loop == odd_set_comp