# Онлайн-школа BEEGEEK 5

m, n = int(input()), int(input())

students = [input() for _ in range(n + m)]
unique = set(students)

both = len(students) - len(unique)

opp = m + n - both * 2
print(opp if opp != 0 else "NO")