# Треугольник Паскаля 1

from math import factorial

n = int(input())

res = []
for m in range(0, n + 1):
    res.append(int(factorial(n) / (factorial(m) * (factorial(n - m)))))

print(res)