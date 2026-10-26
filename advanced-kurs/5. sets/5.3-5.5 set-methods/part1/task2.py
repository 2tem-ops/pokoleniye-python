# Уникальные символы 2

total = set()

for _ in range(int(input())):
    total.update(input().lower())

print(len(total))