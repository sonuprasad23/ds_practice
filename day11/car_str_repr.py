class Car: 
    def __init__(self, make, model, year, num_doors, color="Unknown"):
        self.make = make
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.color = color

    def __str__(self):
        return f"A {self.color} {self.make} {self.model} from {self.year} ({self.num_doors} doors)."

    def __repr__(self):
        return (f"Car(make='{self.make}', model='{self.model}', "
                f"year={self.year}, num_doors={self.num_doors}, color='{self.color}')")

my_car = Car("Honda", "Civic", 2020, 4, "Blue")
print(str(my_car))
print(repr(my_car))
print([my_car]) 