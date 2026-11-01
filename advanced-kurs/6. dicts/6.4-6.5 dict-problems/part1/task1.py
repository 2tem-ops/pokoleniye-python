# Словарь программиста

slang = {}
res = []

for _ in range(int(input())):
    s = input().split(": ")
    slang[s[0].lower()] = s[1]


for _ in range(int(input())):
    res.append(slang.get(input().lower(), "Не найдено"))

print(*res, sep="\n")

