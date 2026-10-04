# Напечатать все цифры из числа

num = 1234
n = len(str(num))

for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10 # формула
    print(digit)

# 1
# 2
# 3
# 4


# Все цифры из числа (наоборот)

num = 496
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num //= 10

# 6
# 9
# 4





# Есть ли цифра в числе?

num = 1576
has_seven = False  # сигнальная метка (флаг)

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')

# YES