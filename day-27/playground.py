# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(1, 2, 3, 4))



# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#     # print(kwargs["add"])
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
#
# calculate(2, add=3, multiply=5)

## REMEMBER
# *args = tuple
# **kwargs = dictionary

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.asdf)

