# Обратный порядок 1

num = int(input())

while num > 0:
    last_digit = num % 10
    print(last_digit)
    num //= 10