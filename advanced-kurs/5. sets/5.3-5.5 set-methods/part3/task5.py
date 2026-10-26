# Урок физики

s1, s2, s3 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()]), set([int(i) for i in input().split()])

print(*sorted(s3 - s2 - s1, reverse=True))