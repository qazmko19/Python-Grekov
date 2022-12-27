fr = open("input.txt", 'r')

a, b, c, d = map(int, fr.read().split(" "))

fr.close()

fw = open("output.txt", 'w')

for x in range(-100, 101):
    if (a * x ** 3) + (b * x ** 2) + (c * x) + d == 0:
        fw.writelines(str(x))
        fw.writelines(" ")

fw.close()
