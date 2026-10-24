# Сортировка чисел

nums = input().split()
res = []

for num in nums:
    res.append(int(num))

res.sort()
print(*res)
res.sort(reverse=True)
print(*res)