# Значение функции

n = int(input())

lst = []
res = []

for _ in range(n):
    num = int(input())
    lst.append(num)
    res.append(num ** 2 + 2 * num + 1)

print(*lst, sep="\n")
print()
print(*res, sep="\n")