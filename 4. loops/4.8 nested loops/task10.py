# Численный треугольник 2

n = int(input())

counter = 1

for i in range(1, n + 1):
    for j in range(i):
        print(counter, " ", end='', sep='')
        counter += 1
    print()