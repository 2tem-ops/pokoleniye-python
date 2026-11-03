# Значение многочлена

from functools import reduce

coeffs = list(map(int, input().split()))
x = int(input())

def evaluate(coefficients: list[int], x: int) -> int:
    total = 0
    for a in coefficients:
        total = total * x + a
    return total

print(evaluate(coeffs, x))
