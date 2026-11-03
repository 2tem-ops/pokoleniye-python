# Интересные числа

a, b = int(input()), int(input())

print(*filter(lambda x: all(int(i) != 0 and x % int(i) == 0 for i in str(x)), range(a, b + 1)))