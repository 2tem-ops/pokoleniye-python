# Звёздный треугольник

def draw_triangle():
    base = 15
    temp = base

    res = []

    for i in range(1, temp, 2):
        res.append("*" * i)
        temp -= 1

    res.append("***************")

    for i in range(len(res)):
        opp = base // 2
        print(" " * opp + res[i])
        base -= 2

draw_triangle()