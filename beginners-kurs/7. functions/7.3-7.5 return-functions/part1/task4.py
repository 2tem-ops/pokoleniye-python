# Математика округлит

from math import ceil, floor

def math_round_to_int(num: float) -> int:
    s = [i for i in str(num).split(".")]
    if s[-1][0] in ["5", "6", "7", "8", "9"]:
        return ceil(num)
    else:
        return floor(num)

print(math_round_to_int(14.489))
