# Сортировка трёх

num1, num2, num3 = int(input()), int(input()), int(input())

highest = max(num1, num2, num3)
lowest = min(num1, num2, num3)
middle = num1 + num2 + num3 - highest - lowest

print(highest, middle, lowest, sep="\n")