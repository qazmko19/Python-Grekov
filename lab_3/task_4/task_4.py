fr = open("input.txt", "r")

move = list(fr.read())

fr.close()

letters = [0, 0]
numbers = [0, 0]
ok = ""

if move[0] == "A":
    letters[0] = 1
elif move[0] == "B":
    letters[0] = 2
elif move[0] == "C":
    letters[0] = 3
elif move[0] == "D":
    letters[0] = 4
elif move[0] == "E":
    letters[0] = 5
elif move[0] == "F":
    letters[0] = 6
elif move[0] == "G":
    letters[0] = 7
elif move[0] == "H":
    letters[0] = 8
else:
    ok = "ERROR"

if move[3] == "A":
    letters[1] = 1
elif move[3] == "B":
    letters[1] = 2
elif move[3] == "C":
    letters[1] = 3
elif move[3] == "D":
    letters[1] = 4
elif move[3] == "E":
    letters[1] = 5
elif move[3] == "F":
    letters[1] = 6
elif move[3] == "G":
    letters[1] = 7
elif move[3] == "H":
    letters[1] = 8
else:
    ok = "ERROR"

numbers[0] = move[1]
numbers[1] = move[4]

if ok != "ERROR":
    dx = abs(int(letters[0]) - int(letters[1]))
    dy = abs(int(numbers[0]) - int(numbers[1]))

    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        ok = "YES"
    else:
        ok = "NO"

fw = open("output.txt", "w")

fw.write(ok)

fw.close()
