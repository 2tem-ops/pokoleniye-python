# Google search - 2

n = int(input())

lst = []
search = []
res = []

for _ in range(n):
    lst.append(input())

requests = int(input())
flag = 0

for _ in range(requests):
    search.append(input())

for i in range(len(lst)):
    for j in range(len(search)):
        if search[j].lower() in lst[i].lower():
            flag += 1
        if flag == requests:
            res.append(lst[i])
    flag = 0

print(*res, sep="\n")


