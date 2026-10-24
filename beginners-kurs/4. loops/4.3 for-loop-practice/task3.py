# Асимптотическое приближение

from math import log, e

n = int(input())
total = 0

for i in range(1, n + 1):
    x = 1 / i
    total += x

print(total - log(n, e))

