# Умножение матриц

n, m1 = [int(i) for i in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
input()

m2, k = [int(i) for i in input().split()]
matrix_2 = [[int(i) for i in input().split()] for _ in range(m2)]

res = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        total_sum = 0
        for r in range(m1):
            total_sum += matrix_1[i][r] * matrix_2[r][j]
        res[i][j] = total_sum

for row in res:
    print(*row)


