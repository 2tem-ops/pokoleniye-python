# Вывести матрицу 1

n = int(input())
m = int(input())

s = [[input() for i in range(m)] for _ in range(n)]

for lst in s:
    print(*lst)

print(s)

