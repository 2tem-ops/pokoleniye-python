# След матрицы

n = int(input())

matrix = []
for _ in range(n):
    s = [int(i) for i in input().split()]
    matrix.append(s)

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

total = 0

for i in range(n):
    total += matrix[i][i]

print(total)