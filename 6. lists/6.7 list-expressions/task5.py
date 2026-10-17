# В одну строку 3

print(*[int(i) ** 2 for i in input().split() if i[-1] != "2" and i[-1] != "8" and int(i) % 2 == 0])