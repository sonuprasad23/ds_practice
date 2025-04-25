e_tuple=()
point=(10,20)
name=("alice",)

print(f"Empty tuple: {e_tuple}, type: {type(e_tuple)}")

print(f"Point tuple: {point}, type: {type(point)}")
print(f"Name tuple: {name}, type: {type(name)}")



#what happens without comma?

not_a_tuple=("Alice")
print(f"Not a tuple :{not_a_tuple}, type: {type(not_a_tuple)}")