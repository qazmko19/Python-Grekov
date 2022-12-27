from math import sqrt

first = int(input("First side -> "))
second = int(input("Second side -> "))
third = int(input("Third side -> "))

p = (first + second + third) / 2
s = sqrt(p * (p - first) * (p - second) * (p - third))

print("Square of this triangle is {}".format(s))
