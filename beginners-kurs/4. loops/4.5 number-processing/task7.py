# Упорядоченные цифры

num = int(input())

flag = "YES"

while num > 0:
    last_digit = num % 10
    num //= 10
    if num != 0:
        cur_digit = num % 10
    if last_digit > cur_digit:
        flag = "NO"

print(flag)