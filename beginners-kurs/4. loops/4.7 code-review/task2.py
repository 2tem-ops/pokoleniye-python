### Ревью кода-2

# Оригинал
n = int(input())
while n > 0:
    n %= 10
print(n)

# Новый код
n = int(input())

while n >= 10:
    n //= 10
print(n)
