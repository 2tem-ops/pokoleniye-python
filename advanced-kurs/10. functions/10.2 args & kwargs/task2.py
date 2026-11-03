def sq_sum(*args: int | float) -> int | float:
    return sum([x ** 2 for x in args])