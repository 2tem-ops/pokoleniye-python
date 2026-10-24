#1
number = int(input())
print(number, number + 1, number + 2, sep="\n")

#2
number1, number2, number3 = int(input()), int(input()), int(input())
summa = number1 + number2 + number3
print(summa)

#3
monitor, pc, keyboard, mouse = int(input()), int(input()), int(input()), int(input())
purchase = monitor + pc + keyboard + mouse
print(purchase * 3)

#4
a, b = int(input()), int(input())
print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)

#5
number = int(input())
print(f"Следующее за числом {number} число: {number + 1}", f"Для числа {number} предыдущее число: {number - 1}", sep="\n")

#6
side = int(input())
print(f"Объем = {side ** 3}", f"Площадь полной поверхности = {6 * side ** 2}", sep="\n")

#7
num1, num2 = int(input()), int(input())
print(f"{num1} + {num2} = {num1 + num2}", f"{num1} - {num2} = {num1 - num2}", f"{num1} * {num2} = {num1 * num2}", sep="\n")

#8
a1, d, n = int(input()), int(input()), int(input())
print(a1 + d * (n - 1))

#9
x = int(input())
print(x, x * 2, x * 3, x * 4, x * 5, sep="---")