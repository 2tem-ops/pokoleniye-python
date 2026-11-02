# Слияние словарей


def merge(values: list[dict[str, int]]) -> dict:
    res = {}
    for value in values:
        for k, v in value.items():
            res.setdefault(k, set()).add(v)
    return res

print(
    merge(
        [
            {'o': 2, 'k': 4},
            {'x': 1},
            {'p': 2},
            {'k': 2, 'j': 5, 'o': 7},
            {'x': 3, 'k': 4, 'j': 2},
        ]
    )
)