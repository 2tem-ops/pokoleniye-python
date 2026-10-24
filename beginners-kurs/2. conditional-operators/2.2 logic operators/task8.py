# Ход короля

# Столбец | Строка
# 4 4 | 5 5 - YES
# 4 4 | 5 4 - YES
# 4 4 | 2 4 - NO

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x2 - x1 == -1 or x2 - x1 == 0 or x2 - x1 == 1) and (y2 - y1 == -1 or y2 - y1 == 0 or y2 - y1 == 1):
    print("YES")
else:
    print("NO")