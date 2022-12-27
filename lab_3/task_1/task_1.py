fr = open("input.txt", "r")

number = int(fr.read())

fr.close()

fw = open("output.txt", "w")

fw.write(str((number // 10) * ((number // 10) + 1)) + "25")

fw.close()
