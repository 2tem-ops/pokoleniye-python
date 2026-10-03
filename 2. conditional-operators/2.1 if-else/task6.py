# Соотношение

num = int(input())

one = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10

if one + thousand == hundred - ten:
    print("ДА")
else:
    print("НЕТ")