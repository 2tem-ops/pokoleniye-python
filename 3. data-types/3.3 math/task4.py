# Тригонометрическое выражение

from math import sin, cos, tan, pi

num = float(input())

x = (num * pi) / 180
result = sin(x) + cos(x) + tan(x) ** 2

print(result)