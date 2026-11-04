from functools import reduce

def product_of_odds(data: list[int]) -> int:
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, data), 1)

print(product_of_odds([3, 3, 3]))