# Побочная диагональ

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][n - i - 1] = 1
        if i + j > n - 1:
            matrix[i][j] = 2

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()