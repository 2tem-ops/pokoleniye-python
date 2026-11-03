from functools import reduce

numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]

print(reduce(lambda x, y: x + y  ** 2, numbers, 0))

