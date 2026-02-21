class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Laptop", 1000)
print(p.price)



class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Ali", 9)
print(s.name, s.grade)
