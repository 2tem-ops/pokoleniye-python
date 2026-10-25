# Заполнение диагоналями

n, m = tuple([int(i) for i in input().split()])

matrix = [[0] * m for _ in range(n)]

nm = 0

for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = nm


for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]:<2}", end=" ")
    print()