# Онлайн-школа BEEGEEK 6

total = int(input())

s1 = []

for _ in range(total):
    urok = int(input())
    for _ in range(urok):
        s1.append(input())

print(*sorted(set([i for i in s1 if s1.count(i) == total])), sep="\n")