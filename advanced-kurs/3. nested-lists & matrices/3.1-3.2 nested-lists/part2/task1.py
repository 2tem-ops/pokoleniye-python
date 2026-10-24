# Список по образцу 1

n = int(input())
res = []

for i in range(1, n + 1):
    res.extend([i])

for i in range(n):
    print(res)