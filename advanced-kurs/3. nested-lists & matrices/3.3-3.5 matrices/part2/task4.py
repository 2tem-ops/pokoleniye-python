# Симметричная матрица

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

    if not symmetric:
        break

if symmetric:
    print("YES")
else:
    print("NO")