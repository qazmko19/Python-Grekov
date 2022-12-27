suma = 0

while True:
    number = int(input("Number -> "))

    if number != 0:
        suma += number
    else:
        break

print("Result is {}".format(suma))
