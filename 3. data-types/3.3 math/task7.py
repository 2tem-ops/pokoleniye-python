# Квадратное уравнение

from math import sqrt

a, b, c = float(input()), float(input()), float(input())

D = b ** 2 - 4 * a * c

x = -(b / (2 * a))
x1, x2 = 0, 0

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)

if D < 0:
    print("Нет корней")
elif D == 0:
    print(x)
else:
    print(min(x1, x2), max(x1, x2), sep="\n")