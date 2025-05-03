numbers = [1,5,10,15,20,25,30]

results_gen = (num//10 for num in numbers if num%10==0)

print(f"Generator object :{results_gen}")
print("Values from iterator:")

for value in results_gen:
    print(value)