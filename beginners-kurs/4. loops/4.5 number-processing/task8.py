# Четные цифры

n = int(input())
digits = len(str(n))
even_cnt = 0

for i in range(1, digits + 1):
    digit = n // 10 ** (digits - i) % 10
    if digit % 2 == 0:
        even_cnt += 1
        print(f"{even_cnt}-я четная цифра равна {digit}")

if even_cnt == 0:
    print("Четных цифр в числе нет")
