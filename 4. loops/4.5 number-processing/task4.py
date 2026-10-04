# Все вместе

num = int(input())

digit_last = num % 10

counter = 0
total = 0
product = 1

first_plus_last = 0

while num > 0:
    last_digit = num % 10
    first_digit = last_digit

    counter += 1
    total += last_digit
    product *= last_digit

    num //= 10

mean = total / counter

print(
    total,
    counter,
    product,
    mean,
    first_digit,
    first_digit + digit_last,
    sep="\n"
)