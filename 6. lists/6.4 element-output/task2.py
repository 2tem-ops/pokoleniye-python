# Без дубликатов

n = int(input())

lst = []

for _ in range(n):
    s = input()
    if s not in lst:
        lst.append(s)

print(*lst, sep="\n")
