# day05/sum_numbers.py
total_sum = 0
for i in range(1, 101):
    total_sum += i # total_sum = total_sum + i
print(f"The sum of numbers from 1 to 100 is: {total_sum}")
# Verification: n*(n+1)/2 = 100*101/2 = 5050