# Переворот строки

with open(input(), "r", encoding="utf-8") as file:
    print(file.readline().strip()[::-1])