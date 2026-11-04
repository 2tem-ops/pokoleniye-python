# Сумма чисел в строках

with open(input(), "r", encoding="utf-8") as file:
    for line in file:
        print(sum(int(i) for i in line.strip().split()))