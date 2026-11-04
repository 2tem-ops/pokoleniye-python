numbers = [(0, 2), (1, 3, 5), (-7, -9, -1)]

print(sorted(numbers, key=lambda item: sum(item) / len(item), reverse=True))