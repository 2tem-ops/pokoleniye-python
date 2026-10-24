# Подсписки списка

s = input().split()
a = []
res = [[]]

for i in range(len(s)):
    for j in range(len(s)):
        a = s[j:i+j+1]
        if len(a) == i+1:
            res.append(a)

print(res)
