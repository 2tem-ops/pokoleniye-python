# Урок биологии

s1, s2, s3 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()]), set([int(i) for i in input().split()])

nums = set(range(1, 11))
res = s1 | s2 | s3

for i in nums:
    if i not in res:
        print(i, end=" ")