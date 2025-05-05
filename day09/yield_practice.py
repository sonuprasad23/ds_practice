def yield_letters(text):
    print("-> Generator starts")

    for char in text:
        print(f"-> Yielding {char}")
        yield char
        print("Generator finished")

print("Iterating through letters ABC")
gen_obj = yield_letters("ABC")

for letter in gen_obj:
    print(f"Received {letter}")

