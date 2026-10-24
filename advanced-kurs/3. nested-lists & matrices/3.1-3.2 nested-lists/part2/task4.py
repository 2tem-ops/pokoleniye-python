# Треугольник Паскаля 2

from math import factorial

def coefficient(n: int) -> list:
    res = []
    for m in range(0, n + 1):
        res.append(int(factorial(n) / (factorial(m) * (factorial(n - m)))))
    return res

n = int(input())

for i in range(n):
    print(*coefficient(i))