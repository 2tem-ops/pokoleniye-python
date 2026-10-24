# Арифметические строки

x, y, z = input(), input(), input()

a, b, c = len(x), len(y), len(z)

if (2 * b - c - a) * (2 * c - b - a) * (2 * a -b - c) == 0:
    print("YES")
else:
    print("NO")