class A:
    def method_a(self):
        print("Method A from class A called.")

class B(A): 
    def method_b(self):
        print("Method B from class B called.")

class C(B): 
    def method_c(self):
        print("Method C from class C called.")


obj_c = C()
obj_c.method_a() 
obj_c.method_b() 
obj_c.method_c()

