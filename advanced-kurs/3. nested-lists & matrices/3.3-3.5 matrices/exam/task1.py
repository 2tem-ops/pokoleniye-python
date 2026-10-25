# Каждый n-ый элемент

s, n = input().split(), int(input())
res = []

for i in range(n):
    res.append(s[i::n])

print(res)