# Удалите нечётные индексы

n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

print(lst[::2])