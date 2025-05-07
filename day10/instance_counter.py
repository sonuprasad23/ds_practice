class CounterObject:
    num_instances = 0

    def __init__(self, name=""):
        self.name = name
        CounterObject.num_instances += 1
        print(f"CounterObject '{name}' created. Total instances: {CounterObject.num_instances}")

print(f"Initial Instances: {CounterObject.num_instances}")
obj_a = CounterObject("A")
obj_b = CounterObject("B")
obj_c = CounterObject()
print(f"Initial Instances: {CounterObject.num_instances}")

