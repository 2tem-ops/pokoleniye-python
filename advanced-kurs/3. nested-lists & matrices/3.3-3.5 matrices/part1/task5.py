n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

res = []

for i in range(n):
    for j in range(n):
        if i >= j:
            res.append(matrix[i][j])

print(max(res))

# [1, 4, 5]
# [6, 7, 8]
# [1, 1, 6]