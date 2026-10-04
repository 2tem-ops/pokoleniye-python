# Последовательность чисел 4

m, n = int(input()), int(input())

if m < n:
    step = 1
    n += 1
else:
    step = -1
    n -= 1

for i in range(m, n, step):
    print(i)
