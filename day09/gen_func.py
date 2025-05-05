def simple_gen():
    print("GEN: Start")
    yield 10
    print("GEN: Resumed after 10")
    yield 20
    print("GEN: Resumed after 20")

    print("GEN: Finished")


gen_obj = simple_gen()
print("Created gen object")
print("Calling next for the first time")

val1= next(gen_obj)
print(f"Received {val1}")

print("Calling next() the 2nd time")

val2 = next(gen_obj)
print(f"Received {val2}")

print("Calling 3rd one")
try:
    val3 = next(gen_obj)
    print(f"Received {val3}")

except StopIteration:
    print("Caught stopiteration as expected")