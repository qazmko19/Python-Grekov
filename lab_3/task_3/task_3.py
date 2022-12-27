fr = open("input.txt", "r")

check = fr.readline()
days = fr.readline().split(" ")

fr.close()

even = []
odd = []

for i in range(int(check)):
    if int(days[i]) % 2 == 0:
        even.append(str(days[i]))
    else:
        odd.append(str(days[i]))

if len(even) > len(odd):
    ok = "YES"
else:
    ok = "NO"

fw = open("output.txt", "w")

for i in range(len(odd)):
    fw.write(odd[i])
    fw.write(" ")
fw.write("\n")

for i in range(len(even)):
    fw.write(even[i])
    fw.write(" ")
fw.write("\n")

fw.write(ok)

fw.close()
