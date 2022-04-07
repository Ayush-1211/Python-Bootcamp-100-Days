def add(*args):
    print(args)
    print(type(args))
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print("Sum: ", add(3,4,5,6))

print("---------------------------------------------------")

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

print("---------------------------------------------------")

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.seats = kw.get("seats")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.color)