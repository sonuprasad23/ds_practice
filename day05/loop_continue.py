# day05/loop_continue.py
print("Printing odd numbers (1-10):")
for i in range(1, 11):
    if i % 2 == 0:
        continue # Skip the rest of this iteration, go to next i
    print(i)