# Возведение матрицы в степень

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

res = [row[:] for row in matrix]


for _ in range(m - 1):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += res[i][k] * matrix[k][j]

    res = temp

for row in res:
    print(*row)