# Remove outliers

n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

lst.remove(max(lst))
lst.remove(min(lst))
print(*lst, sep="\n")
