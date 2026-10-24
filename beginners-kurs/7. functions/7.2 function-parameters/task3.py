# Сумма цифр

def print_digit_sum(num: int):
    total = 0

    while num != 0:
        last_digit = num % 10
        total += last_digit
        num //= 10
    print(total)

print_digit_sum(123)

