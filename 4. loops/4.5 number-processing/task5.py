# Вторая цифра

n = int(input())
i = 2

digits = len(str(n))
digit = n // 10 ** (digits - i) % 10

print(digit)


