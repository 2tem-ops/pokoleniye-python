# Суммы двух

n = int(input())

lst = []
result = []

for i in range(n):
    lst.append(int(input()))

for i in range(len(lst) - 1):
    result.append(lst[i] + lst[i + 1])

print(result)
