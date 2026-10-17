# Временной промежуток

h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input())

hm1 = h1 * 60 + m1
hm2 = h2 * 60 + m2

for i in range(hm1, hm2 + 1):
    hours, mins = i // 60, i % 60
    print(f"{hours:02d}:{mins:02d}")
