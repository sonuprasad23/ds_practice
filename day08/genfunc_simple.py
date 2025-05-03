def count_up_to(n):
    print("Generator Started")
    i=0
    while i<n:
        print(f"Yielding {i}")
        yield i
        i+=1
        print("Generator Resumed")
    print("Generator Finished")

counter_gen = count_up_to(3)
print(f"Generator object: {counter_gen}")

print("\nIterating with for loop: ")

for number in counter_gen:
    print(f"Received: {number} from the loop")

print("\nTrying to iterate again: (iterator exhausted)")
for number in counter_gen:
    print(f"Received: {number} second time")

print("\nManual Iteration: ")

counter_gen_manual = count_up_to(2)

try:
    print(f"Manual next(): {next(counter_gen_manual)}")
    print(f"Manual next(): {next(counter_gen_manual)}")
    print(f"Manual next(): {next(counter_gen_manual)}") # Raises StopIteration
except StopIteration:
    print("StopIteration caught!")