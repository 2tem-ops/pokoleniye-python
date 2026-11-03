abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))

print(all(i[0] ** 2 + i[1] ** 2 + i[2] ** 2 <= 4 for i in zip(abscissas, ordinates, applicates)))

