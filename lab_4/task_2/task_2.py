fr = open("input.txt", "r")

numbers = fr.read().split(" ")

fr.close()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a * b == c:
    res = "YES"
else:
    res = "NO"

fw = open("output.txt", "w")

fw.write(res)

fw.close()
