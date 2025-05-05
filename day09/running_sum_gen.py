def running_sum_gen(numbers):
    current_sum = 0
    for num in numbers:
        current_sum+=num
        yield current_sum

print("Running sums for [1,2,3,4]")

for r_sum in running_sum_gen([1,2,3,4]):
    print(r_sum)