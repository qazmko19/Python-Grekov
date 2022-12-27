time = int(input("Time for sleep in minutes -> "))
hours = int(input("Hours, when Katya goes to bed -> "))
minutes = int(input("Minutes, when Katya goes to bed -> "))

res1 = int((time + minutes) / 60)
res2 = int((time + minutes) % 60)

print(res1 + hours)
print(res2)
