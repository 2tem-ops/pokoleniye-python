# Самописный калькулятор

num1, num2, operator = int(input()), int(input()), input()

if operator == "*":
    print(num1 * num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
else:
    print("Неверная операция")

