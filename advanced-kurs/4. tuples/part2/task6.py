# Конкурсный отбор

n = int(input())
res = []

for _ in range(n):
    res.append(input().split())

for student in res:
    print(" ".join(student))

print()

for student in res:
    if student[-1] == "4" or student[-1] == "5":
        print(" ".join(student))