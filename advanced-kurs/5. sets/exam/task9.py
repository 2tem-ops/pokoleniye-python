# Онлайн-школа BEEGEEK 3

m, n = int(input()), int(input())

math_stud = {input() for _ in range(m)}
info_stud = {input() for _ in range(n)}

opp = len(math_stud) - len(math_stud & info_stud) + len(info_stud) - len(math_stud & info_stud)
print(opp if opp != 0 else "NO")