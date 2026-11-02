# Сумма дробей 1

from fractions import Fraction as F

n = int(input())

total = F(1, 1 ** 2)

for i in range(2, n + 1):
    total += F(1, i ** 2)

print(total)