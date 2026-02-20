def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))

def print_args(*args):
    for i in args:
        print(i)
print_args("A", "B", "C")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
print_info(name="Aruzhan", age=16)