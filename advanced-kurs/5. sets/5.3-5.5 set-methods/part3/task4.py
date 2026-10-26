# Урок математики

s1, s2, s3 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()]), set([int(i) for i in input().split()])

print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3)))