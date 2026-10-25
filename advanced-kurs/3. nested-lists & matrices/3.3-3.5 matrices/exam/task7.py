# Ход ферзя

moves = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
move = input()

coord1 = 8 - int(move[1])
coord2 = moves[move[0]]

chessboard = [["."] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        chessboard[coord1][coord2] = "Q"
        if j == coord2 or i == coord1:
            chessboard[i][j] = "*"
        if coord1 + coord2 == i + j or coord1 - coord2 == i - j:
            chessboard[i][j] = "*"

for row in chessboard:
    print(" ".join(row))