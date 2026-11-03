# Математические функции

from math import sin, sqrt

funcs = {"квадрат": lambda x: x ** 2,
         "модуль": abs,
         "куб": lambda x: x ** 3,
         "корень": sqrt,
         "синус": sin
         }

num, func = int(input()), input()

print(funcs[func](num))