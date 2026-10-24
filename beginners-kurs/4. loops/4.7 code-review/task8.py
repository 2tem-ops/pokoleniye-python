### Ревью кода-6

# Оригинал
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)

# Новый код
maximum = -10
total = 0

for _ in range(10):
    num = int(input())
    if num < 0:
        total += num
        if num >= maximum:
            maximum = num

if total:
    print(total, maximum, sep="\n")
else:
    print("NO")