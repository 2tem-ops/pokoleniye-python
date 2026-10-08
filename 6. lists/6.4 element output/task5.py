# Google search - 1

n = int(input())

lst = []

for _ in range(n):
    lst.append(input())

search = input().lower()

for s in lst:
    if search in s.lower():
        print(s)