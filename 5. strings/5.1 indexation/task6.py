# Цифра 2

s = input()
num = False

for c in s:
    if c.isdigit():
        num = True

if num:
    print("Цифра")
else:
    print("Цифр нет")