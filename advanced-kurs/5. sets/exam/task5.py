# Книги на прочтение

m, n = int(input()), int(input())
s1 = {input() for _ in range(m)}

for _ in range(n):
    book = input()
    print("YES" if book in s1 else "NO")