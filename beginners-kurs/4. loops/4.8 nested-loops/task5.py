# Звёздный треугольник

n = int(input()) # нечётное

for i in range(n // 2):
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(n // 2, 0, -1):
   for j in range(i + 1):
        print("*", end="")
   print()
print("*")