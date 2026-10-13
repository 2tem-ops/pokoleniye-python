#1
num = int(input())
hundred = num // 100
ten = (num % 100) // 10
one = num % 10
print(f"Сумма цифр = {hundred + ten + one}")
print(f"Произведение цифр = {hundred * ten * one}")

#2
abc = int(input())
a = str(abc // 100)
b = str((abc % 100) // 10)
c = str(abc % 10)
print(a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a, sep="\n")

#3
number = int(input())
thousand = number // 1000
hundred = (number % 10 ** 3) // 10 ** 2
ten = (number % 100) // 10
one = number % 10
print(f"Цифра в позиции тысяч равна {thousand}", f"Цифра в позиции сотен равна {hundred}", f"Цифра в позиции десятков равна {ten}", f"Цифра в позиции единиц равна {one}", sep="\n")