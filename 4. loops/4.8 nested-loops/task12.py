# Сумма факториалов

n = int(input())
n_factorial = 1
total = 0

for i in range(1, n + 1):
    n_factorial *= i
    total += n_factorial

print(total)