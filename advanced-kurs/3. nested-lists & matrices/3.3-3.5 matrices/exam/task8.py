# Диагонали, параллельные главной

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distance = abs(i - j)
        matrix[i][j] = distance

for row in matrix:
    print(*row)

