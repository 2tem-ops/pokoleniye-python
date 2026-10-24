#1 Геометрическая прогрессия
b1, q, n = int(input()), int(input()), int(input())
print(b1 * q ** (n-1))

#2 Число метров по заданному числу сантиметров
cm = int(input())
m = cm // 100
print(m)

#3 Задача про мандарины и школьников
pupils = int(input())
mandarins = int(input())
print(mandarins // pupils)
print(mandarins % pupils)

#4 Задача про Таноса
pop = int(input())
print(pop // 2 + pop % 2)

#5 Время
minutes = int(input())
print(f"{minutes} мин - это {minutes // 60} час {minutes % 60} минут")
