numbers = [7, -6, 23, 287, -147, -26, 3]

print(sum(map(lambda x: x ** 2, filter(lambda x: len(str(abs(x))) == 2 and x % 7 == 0, numbers))))