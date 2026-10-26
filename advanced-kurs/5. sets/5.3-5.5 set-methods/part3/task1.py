# Одинаковые цифры

n1, n2 = set(input()), set(input())

print("NO" if n1.isdisjoint(n2) else "YES")
