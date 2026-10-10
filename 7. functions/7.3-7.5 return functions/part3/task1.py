# Середина отрезка

def get_middle_point(x1: int, y1: int, x2: int, y2: int):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

print(*get_middle_point(0, 0, 10, 0))
print(*get_middle_point(1, 5, 8, 3))