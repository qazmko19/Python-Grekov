number = int(input("Number -> "))

interval1 = range(-14, 13)
interval2 = range(15, 17)
interval3 = range(19, 100)

print(number in interval1 or number in interval2 or number in interval3)
