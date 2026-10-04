# Цифровые сообщения

# Оригинал
num = int(input())
cnt = 0
total = 0
while num % 100 != 11:
    if len(num) > 7:
        cnt += 1

    total =+ 1
    num = int(input())

print(cnt, '/', total, sep='')

# Новый код
num = int(input())
cnt = 0
total = 0

while num % 100 != 11:
    if len(str(num)) > 7:
        cnt += 1

    total += 1
    num = int(input())

if num % 100 == 11:
    total += 1

if len(str(num)) > 7:
    cnt += 1


print(cnt, total, sep='/')