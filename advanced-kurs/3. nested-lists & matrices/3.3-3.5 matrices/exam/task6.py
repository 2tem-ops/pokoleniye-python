#  Латинский квадрат

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = True

for row in matrix:
    if sorted(row) != list(range(1, n + 1)):
        flag = False
        break

for j in range(n):
    column = [matrix[i][j] for i in range(n)]
    if sorted(column) != list(range(1, n + 1)):
        flag = False
        break

print("YES" if flag else "NO")