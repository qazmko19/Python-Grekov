fr = open("input.txt", "r")

length = int(fr.readline())
numbers = fr.readline().split(" ")

for i in range(length):
    numbers[i] = int(numbers[i])

positive_sum = 0
multiplication = 1

min_el = 0
max_el = 0

for i in range(length):
    if numbers[i] >= 0:
        positive_sum += numbers[i]
    if numbers[i] < numbers[min_el]:
        min_el = i
    if numbers[i] > numbers[max_el]:
        max_el = i

for i in range(length):
    if min_el < i < max_el or min_el > i > max_el:
        multiplication *= numbers[i]

result = "{} {}".format(positive_sum, multiplication)

fw = open("output.txt", "w")

fw.write(result)

fw.close()
