fr = open("input.txt", "r")

count = fr.read().split(" ")

fr.close()

final = 0

for i in range(len(count)):
    if int(count[i]) > int(final):
        final = count[i]

fw = open("output.txt", "w")

fw.write(final)

fw.close()
