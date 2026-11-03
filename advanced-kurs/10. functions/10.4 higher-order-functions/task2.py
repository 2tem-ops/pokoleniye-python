numbers = [854, 10, 5, 452, 478, 236, 202, 41]

print(*[i ** 3 for i in filter(lambda x: len(str(x)) == 3 and x % 5 == 2, numbers)], sep="\n")