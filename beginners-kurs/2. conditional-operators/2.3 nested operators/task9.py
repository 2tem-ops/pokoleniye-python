# Пересечение отрезков

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# Находим границы пересечения
left = max(a1, a2)
right = min(b1, b2)

# Определяем результат
if left < right:
    print(left, right)  # пересечение - отрезок
elif left == right:
    print(left)  # пересечение - точка
else:
    print("пустое множество")  # пересечения нет