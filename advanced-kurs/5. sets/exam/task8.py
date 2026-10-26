# Онлайн-школа BEEGEEK 2

m, n = int(input()), int(input())
math_stud = set()
info_stud = set()

for _ in range(m):
    math_stud.add(input())

for _ in range(n):
    info_stud.add(input())

print(len(math_stud - info_stud))