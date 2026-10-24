n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

check = []
for row in matrix:
    check.extend(row)

factorial = list(range(1, n ** 2 + 1))
are_equal = sorted(check) == factorial

rows = [0] * n
columns = [0] * n
main_diagonal = 0
sec_diagonal = 0

for i in range(n):
    for j in range(n):
        rows[i] += matrix[i][j]
        columns[j] += matrix[i][j]

    main_diagonal += matrix[i][i]
    sec_diagonal += matrix[i][n - i - 1]

target = rows[0]

sums_equal = True

for i in range(n):
    if rows[i] != target or columns[i] != target:
        sums_equal = False

if main_diagonal != target or sec_diagonal != target:
    sums_equal = False

print("YES" if sums_equal and are_equal else "NO")