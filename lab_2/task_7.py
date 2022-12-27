while True:
    number = int(input("Number -> "))

    if number < 10:
        continue
    elif number > 100:
        break
    else:
        print("Your number is {}".format(number))
