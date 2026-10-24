# Звёздный прямоугольник
print("*" * 17, "*" + " " * 15 + "*", "*" + " " * 15 + "*", "*" * 17, sep="\n")

# Квадрат суммы VS Сумма квадратов
num1, num2 = int(input()), int(input())
square_of_sum = (num1 + num2) ** 2
sum_of_square = num1 ** 2 + num2 ** 2
print(f"Квадрат суммы {num1} и {num2} равен {square_of_sum}", f"Сумма квадратов {num1} и {num2} равна {sum_of_square}", sep="\n")

# Большое число
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a ** b + c ** d)

# Размножение n-ок
num = int(input())
temp = str(num)
temp2 = temp * 2
temp3 = temp * 3
result = int(temp) + int(temp2) + int(temp3)
print(result)