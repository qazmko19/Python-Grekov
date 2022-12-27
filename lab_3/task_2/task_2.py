fr = open("input.txt", "r")

number = fr.read()

fr.close()

fw = open("output.txt", "w")

fw.write(number + "9" + str(9 - int(number)))

fw.close()
