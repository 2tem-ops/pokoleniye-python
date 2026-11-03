numbers = [(0, 0), (1, 1), (2, 2, 2), (3,)]

print(min(numbers, key=lambda i: sum(i) / len(i)), max(numbers, key=lambda i: sum(i) / len(i)), sep="\n")