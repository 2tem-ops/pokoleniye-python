# k-ая буква слова

n = int(input())

lst = []
res = ""

for _ in range(n):
    lst.append(input())

k = int(input())

for c in lst:
    if k <= len(c):
        res += c[k - 1]

print(res)