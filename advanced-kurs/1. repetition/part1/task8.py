# power of 2: w(n) = 1

# (n = 13, 2^a = 8, l = 5)
# w(n) = 2l + 1 (10 + 1),
# ex: n = 41, 2^a = 32, l = 9 (2l + 1 = 19)

# 41 = 101001
# take first digit and write at end:
# 010011 = 19 = 2l + 1

# Задача Иосифа Флавия

n = int(input())
k = int(input())
lst = [i for i in range(1, n + 1)]

while len(lst) > 1:
    for i in range(k - 1):
        lst.append(lst.pop(0))
    lst.pop(0)

print(lst[0])

