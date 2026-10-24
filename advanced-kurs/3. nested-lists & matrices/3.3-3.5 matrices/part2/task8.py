# Ходы коня

# [* . * . . . . .]
# [. . . * . . . .]
# [. N . . . . . .]
# [. . . * . . . .]
# [* . * . . . . .]
# [. . . . . . . .]
# [. . . . . . . .]
# [. . . . . . . .]
moves = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
move = input()

coord1 = 8 - int(move[1])
coord2 = moves[move[0]]

chessboard = [["."] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        dx = abs(coord1 - i)
        dy = abs(coord2 - j)

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            chessboard[i][j] = "*"
        chessboard[coord1][coord2] = "N"

for row in chessboard:
    print(" ".join(row))