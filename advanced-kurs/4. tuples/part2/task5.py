# Вершина параболы

a, b, c = int(input()), int(input()), int(input())

coord1 = -(b / (2*a))
coord2 = (4 * a * c - b ** 2) / (4 * a)

print((coord1, coord2))