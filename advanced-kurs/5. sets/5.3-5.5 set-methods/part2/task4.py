# Общие цифры

n = int(input())

res = set(input())
for _ in range(n - 1):
    a = set(input())
    res.intersection_update(a)

print(*sorted(res))