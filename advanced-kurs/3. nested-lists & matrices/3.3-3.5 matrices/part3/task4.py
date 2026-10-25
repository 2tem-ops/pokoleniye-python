# Заполнение 2

n, m = tuple([int(i) for i in input().split()])
matrix = [[0] * m for _ in range(n)]

k = 1
for j in range(m):
    for i in range(n):
        matrix[i][j] = k
        k += 1

for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]:<2}", end=" ")
    print()