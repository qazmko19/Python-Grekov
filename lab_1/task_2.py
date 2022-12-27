time = int(input("Time for sleep in minutes -> "))
hours = int(time / 60)
minutes = int(time % 60)

print("Kolya need to set alarm for {}:{}".format(hours, minutes))
