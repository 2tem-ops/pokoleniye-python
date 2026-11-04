# Обратный порядок

with open(input(), "r", encoding="utf-8") as file:
    lines = file.readlines()[::-1]
    for line in lines:
        print(line.rstrip())