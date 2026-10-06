# Числа Рамануджана

for a in range(1, 35):
    for b in range(a + 1, 35):
        for c in range(a + 1, 35):
            for d in range(c + 1, 35):
                if (a ** 3 + b ** 3) == (c ** 3 + d ** 3):
                    print(a ** 3 + b ** 3)