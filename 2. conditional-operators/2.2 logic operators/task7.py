# Ход ладьи

# Столбец | Строка
# 4 4 | 5 4 - YES
# 4 4 | 4 5 - YES
# 4 4 | 5 5 - NO
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 != x2 and y1 == y2) or (y1 != y2 and x1 == x2):
    print("YES")
else:
    print("NO")

