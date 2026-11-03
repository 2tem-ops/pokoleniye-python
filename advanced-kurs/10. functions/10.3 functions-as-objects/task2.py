from math import sqrt

points = [(3, 4), (-2, 1), (0, 1), (5, 12)]

print(sorted(points, key=lambda xy: sqrt(xy[0] ** 2 + xy[1] ** 2)))

