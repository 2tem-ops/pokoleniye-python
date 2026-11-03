numbers = [(1, 5), (0, -1, 3), (5, 7, 15)]

print(sorted(numbers, key=lambda x: max(x) + min(x)))