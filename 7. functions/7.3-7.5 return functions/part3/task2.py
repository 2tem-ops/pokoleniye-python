# Площадь и длина

from math import pi

def get_circle(radius: int | float):
    c = 2 * pi * radius
    s = pi * radius ** 2
    return c, s

print(*get_circle(1))
print(*get_circle(1.5))