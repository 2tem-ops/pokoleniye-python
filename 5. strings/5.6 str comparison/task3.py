# Необычное сравнение

s1, s2 = input(), input()
result1, result2 = "", ""

for c in s1:
    if c.isalpha():
        result1 += c

for c in s2:
    if c.isalpha():
        result2 += c

result1 = result1.lower().replace(" ", "")
result2 = result2.lower().replace(" ", "")

if result1 == result2:
    print("YES")
else:
    print("NO")
