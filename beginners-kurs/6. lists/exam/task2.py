# Сумма двух списков

s1, s2 = input().split(), input().split()

L = []
M = []
res = []

for num in s1:
    L.append(int(num))

for num in s2:
    M.append(int(num))

for i in range(len(L)):
    res.append(L[i] + M[i])

print(*res)
