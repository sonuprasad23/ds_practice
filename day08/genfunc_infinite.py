def infinite_counter(start=0):
    num=start
    while True:
        yield num
        num+=1

print("First 5 numbers from infinite counter:")
count = 0

for number in infinite_counter(10):
    print(number)
    count+=1
    if count>=5:
        break