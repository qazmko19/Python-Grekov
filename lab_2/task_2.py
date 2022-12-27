import math
from math import sqrt


def triangle():
    a = int(input("First side -> "))
    b = int(input("Second side -> "))
    c = int(input("Third side -> "))

    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def rectangle():
    a = int(input("First side -> "))
    b = int(input("Second side -> "))

    return a * b


def circle():
    r = int(input("Radius -> "))

    return math.pi * r ** 2


type_input = input("Type -> ")

if type_input == "triangle":
    print(triangle())
elif type_input == "rectangle":
    print(rectangle())
elif type_input == "circle":
    print(circle())
else:
    print("Wrong type!")
