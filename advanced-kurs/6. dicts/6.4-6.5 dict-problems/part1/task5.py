# Страны и города

cities = {}

for _ in range(int(input())):
    lst = input().split()
    cities[lst[0]] = lst[1:]

for _ in range(int(input())):
    find = input()
    print(*[k[0] for k in cities.items() if find in k[1]])
