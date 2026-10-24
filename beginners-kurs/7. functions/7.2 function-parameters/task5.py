# Звёздный треугольник

def draw_triangle(fill: str, base: int):
    for i in range(base // 2):
        print(fill * (i + 1))

    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))

draw_triangle("+", 9)