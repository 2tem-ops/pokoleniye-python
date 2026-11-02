from random import uniform

n = 10**6       # количество испытаний
k = 0
s0 = 16

for _ in range(n):
    x = uniform(-2.0, 2.0)
    y = uniform(-2.0, 2.0)

    if 3 * x + y ** 2 <= 2 and x ** 3  + y ** 4 + 2 >= 0:
        k += 1

print((k/n)*s0)


