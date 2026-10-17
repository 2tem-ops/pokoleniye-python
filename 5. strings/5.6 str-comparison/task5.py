# Название класса

n = int(input())

for i in range(n):
    cls = input()
    if cls[0].isdigit() and len(cls) == 2 and 1040 <= ord(cls[-1]) <= 1055:
        print("YES")
    else:
        print("NO")


