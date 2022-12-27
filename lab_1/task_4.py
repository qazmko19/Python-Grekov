year = int(input("Year -> "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is leap year".format(year))
        else:
            print("{} is not leap year".format(year))
    else:
        print("{} is leap year".format(year))
else:
    print("{} is not leap year".format(year))
