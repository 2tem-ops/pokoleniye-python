# Шахматная доска

n, m = tuple([int(i) for i in input().split()])
matrix = [["."] * m for _ in range(n)]

for i in range(n):
    for j in range(0, m, 2):
        if i % 2 == 0:
            j += 1

        if j < m:
            matrix[i][j] = "*"

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()