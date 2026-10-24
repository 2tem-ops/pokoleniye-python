# Индекс массы тела

m, p = float(input()), float(input())

def imt(m: float, p: float) -> str:
    calc = m / (p * p)
    if 18.5 <= calc <= 25:
        return "Оптимальная масса"
    elif calc < 18.5:
        return "Недостаточная масса"
    else:
        return "Избыточная масса"

print(imt(m, p))