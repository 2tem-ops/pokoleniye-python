### Ревью кода-3

# Оригинал
s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)

# Новый код
total = 0

for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        total += n
print(total)
