# Заполнение змейкой

n, m = tuple([int(i) for i in input().split()])
matrix = [[0] * m for i in range(n)]

k = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = k
        k += 1

for index, row in enumerate(matrix):
    if index % 2 != 0:
        row.reverse()

for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]:<2}", end=" ")
    print()