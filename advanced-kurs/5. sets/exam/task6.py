# Странное увлечение

s1, s2 = {int(i) for i in input().split()}, {int(i) for i in input().split()}

if len(s1 & s2) == 0:
    print("BAD DAY")
else:
    print(*sorted(s1 & s2, reverse=True))