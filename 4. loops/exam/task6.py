# Все вместе 2

n = int(input())
last_digit = n % 10

last_digit_count = 0
three_count = 0
even_count = 0
zero_five_count = 0

product = 1
total = 0

while n != 0:
    if n % 10 > 7:
        product *= n % 10

    if n % 10 > 5:
        total += n % 10

    if n % 10 == last_digit:
        last_digit_count += 1

    if n % 10 == 3:
        three_count += 1

    if n % 10 == 0 or n % 10 == 5:
        zero_five_count += 1

    if n % 10 % 2 == 0:
        even_count += 1

    n //= 10

print(
    three_count, last_digit_count, even_count,
    total, product, zero_five_count, sep="\n"
)
