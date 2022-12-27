number1 = int(input("First number -> "))
number2 = int(input("Seond number -> "))
op = input("Operation (+, -, *, /, mod, pow, div) -> ")

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "/":
    if number2 == 0:
        print("Second number is 0. Cannot be divided by 0!")
    else:
        print(number1 / number2)
elif op == "mod":
    if number2 == 0:
        print("Second number is 0. Cannot be divided by 0!")
    else:
        print(number1 % number2)
elif op == "pow":
    print(number1 ** number2)
elif op == "div":
    if number2 == 0:
        print("Second number is 0. Cannot be divided by 0!")
    else:
        print(number1 // number2)
else:
    print("Wrong operation!")
