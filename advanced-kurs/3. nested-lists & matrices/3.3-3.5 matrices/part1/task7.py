# Суммы четвертей

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

left, right, up, down = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i > j and i < (n - 1 - j):
            left += matrix[i][j]
        if i < j and i > (n - 1 - j):
            right += matrix[i][j]
        if i > j and i > (n - 1 - j):
            down += matrix[i][j]
        if i < j and i < (n - 1 - j):
            up += matrix[i][j]

print(f"Верхняя четверть: {up}")
print(f"Правая четверть: {right}")
print(f"Нижняя четверть: {down}")
print(f"Левая четверть: {left}")
