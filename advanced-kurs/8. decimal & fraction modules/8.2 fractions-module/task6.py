# Сумма дробей 2

from math import factorial
from fractions import Fraction as F

n = int(input())
total = F(1, 1)

for i in range(2, n + 1):
    total += F(1, factorial(i))

print(total)

