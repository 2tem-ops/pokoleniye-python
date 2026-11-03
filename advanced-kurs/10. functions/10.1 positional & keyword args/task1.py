def matrix(rows: int | None=None, cols: int | None=None, value: int=0):
    if rows is None and cols is None:
        return [[value] * 1 for _ in range(1)]
    elif cols is None:
        return [[value] * rows for _ in range(rows)]
    return [[value] * cols for _ in range(rows)]

print(matrix(3, 4, 9))