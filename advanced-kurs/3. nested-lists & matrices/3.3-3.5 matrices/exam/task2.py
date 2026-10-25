# Максимальный в области 2

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

maximum = -10000

for i in range(n):
    for j in range(n):
        if i + j >= n - 1:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)