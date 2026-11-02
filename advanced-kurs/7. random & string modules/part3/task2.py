from random import uniform

n = 10**6 # количество испытаний
circle = 0

for _ in range(n):
    x, y = uniform(-1, 1), uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:
        circle += 1

print((circle / n) * 4)


