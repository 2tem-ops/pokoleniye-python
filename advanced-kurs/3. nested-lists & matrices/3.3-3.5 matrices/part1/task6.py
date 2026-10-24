# Максимальный в области 2

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

res = []
for i in range(n):
    for j in range(n):
        res.append(matrix[i][i])
        res.append(matrix[i][n-i-1])
        if (i > j and i < (n - 1 - j)) or (i < j and i > (n - 1 - j)):
            res.append(matrix[i][j])

print(max(res))