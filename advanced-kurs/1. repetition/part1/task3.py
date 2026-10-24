# Стоимость строки

s = input()

total = 0

for _ in range(len(s)):
    total += 60

print(f"{total // 100} р. {total % 100} коп.")