# Урок информатики

s1, s2, s3 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()]), set([int(i) for i in input().split()])

# есть у s1 и s2, нету у s3

s1_s2 = s1 & s2

res = {i for i in s1_s2 if i not in s3}
print(*sorted(res, reverse=True))