# Ревью кода-7

n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        last_digit = n % 10
        s += last_digit
    n //= 10

if s:
    print(s)
else:
    print(0)