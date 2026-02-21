products = [("Phone", 300), ("Laptop", 1000), ("Mouse", 20)]
print(sorted(products, key=lambda x: x[1]))

names = ["Ali", "Christopher", "Dana"]
print(sorted(names, key=lambda x: len(x)))
