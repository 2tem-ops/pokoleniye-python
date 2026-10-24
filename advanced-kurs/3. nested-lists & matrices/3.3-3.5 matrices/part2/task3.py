# Обмен столбцов

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

i, j = tuple([int(i) for i in input().split()])

for k in range(len(matrix)):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()