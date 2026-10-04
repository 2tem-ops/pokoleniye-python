### Ревью кода-1

# Оригинал
n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)


# Новый код
n = int(input())

product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print(product)