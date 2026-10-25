# Снежинка

n = int(input())
board = [["."] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        board[i][i] = "*"
        board[i][n-i-1] = "*"
        if j == n // 2:
            board[i][j] = "*"
        if i == n // 2:
            board[i][j] = "*"

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()