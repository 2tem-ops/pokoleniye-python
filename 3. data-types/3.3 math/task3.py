# Евклидово расстояние

from math import sqrt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

euclidean = sqrt((x2-x1)**2 + (y2-y1)**2)
print(euclidean)