### Ревью кода-4

# Оригинал
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')

# Новый код
count = 0
product = 1

for _ in range(0, 10):
    num = int(input())

    if num >= 0:
        product *= num
        count += 1

if count > 0:
    print(count, product, sep="\n")
else:
    print('NO')
