class Book:
    material = "paper"
    has_cover = True

book1 = Book()
book2 = Book()

print(f"book1 material: {book1.material}")
print(f"book2 material: {book2.material}")
print(f"Book class material : {Book.material}")


#Change class attribute
Book.material = "recycled paper"
print(f"Book1 material after class change: {book1.material}")
print(f"Book2 material after class change: {book2.material}")