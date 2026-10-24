# Средние значения

from math import sqrt

a, b = float(input()), float(input())

mean = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_mean = (2 * a * b) / (a + b)
square_mean = sqrt((a ** 2 + b ** 2) / 2)

print(mean, geometric_mean, harmonic_mean, square_mean, sep="\n")