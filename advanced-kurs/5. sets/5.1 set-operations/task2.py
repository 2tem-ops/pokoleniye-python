# Книги на прочтение

n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

b = n + m - t - x
c = m + k - t - y
d = n + k - t - z

one = (k - d - c - t) + (n - d - b - t) + (m - b - c - t)
two = b + c + d
none = a - (one + two) - t

print(one, two, none, sep="\n")