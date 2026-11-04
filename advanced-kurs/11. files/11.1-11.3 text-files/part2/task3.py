# Длинные строки

with open(input(), "r", encoding="utf-8") as file:
    lines = file.readlines()
    length = len(max(lines, key=len))
    print(*[i.rstrip() for i in filter(lambda x: len(x) == length, lines)], sep="\n")