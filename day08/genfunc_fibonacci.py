def fibonacci_gen(limit):
    a,b=0,1
    while a<=limit:
        yield a 
        a,b=b,a+b

print("Fibonacci numbers up to 50:")
for fib_num in fibonacci_gen(50):
    print(fib_num, end=" ")

print()