# Максимум в таблице

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

maximum = -9999
coords = ()

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            coords = (i, j)

print(*coords)
