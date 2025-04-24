# day05/loop_break.py
print("Searching for 7:")
for i in range(1, 11):
    if i == 7:
        print("Found 7!")
        break # Exit the loop immediately
    print(i)