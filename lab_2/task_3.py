count_list = list(input("Count of workers -> "))
count = "".join(count_list)

if count_list[-1] == "0":
    print("{} программистов".format(count))
elif count_list[-1] == "1":
    if int(count) in range(11, 1000, 100):
        print("{} программистов".format(count))
    else:
        print("{} программист".format(count))
elif count_list[-1] == "2" or count_list[-1] == "3" or count_list[-1] == "4":
    if int(count) in range(12, 1000, 100) or int(count) in range(13, 1000, 100) or int(count) in range(14, 1000, 100):
        print("{} программистов".format(count))
    else:
        print("{} программиста".format(count))
elif count_list[-1] >= "5":
    print("{} программистов".format(count))
else:
    print("Wrong!")
