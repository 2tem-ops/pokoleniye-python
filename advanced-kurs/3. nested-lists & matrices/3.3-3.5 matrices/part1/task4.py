# Больше среднего

n = int(input())
matrix = []
res = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

# [1, 2, 3, 4]
# [5, 6, 3, 15]
# [0, 2, 3, 1]
# [5, 2, 8, 5]

for row in matrix:
    count = 0
    for elem in row:
        if elem > sum(row) / n:
            count += 1
    res.append(count)

for i in res:
    print(i)
