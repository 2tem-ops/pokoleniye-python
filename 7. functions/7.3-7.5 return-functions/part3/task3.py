# Корни уравнения

from math import sqrt

def solve(a: int, b: int, c: int):
    d = b ** 2 - (4 * a * c)

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = x1

    return min(x1, x2), max(x1, x2)

print(*solve(1, -4, -5))
print(*solve(-2, 7, -5))
print(*solve(1, 2, 1))