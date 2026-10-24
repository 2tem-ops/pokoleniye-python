# Сумма чисел

s = input().split()
res = "+".join(s)

print(res, "=", *[sum(int(i) for i in s)], sep="")