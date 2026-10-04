### Ревью кода-5

# Оригинал
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)

# Новый код
n = int(input())
max_digit = 0
counter = 0

while n > 0:
    digit = n % 10

    if digit % 3 == 0:
        counter += 1
        if digit > max_digit:
            max_digit = digit

    n //= 10

if counter == 0:
    print('NO')
else:
    print(max_digit)
