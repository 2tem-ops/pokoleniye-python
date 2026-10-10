# Биномиальный коэффициент

from math import factorial

def compute_binom(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial((n - k)))

print(compute_binom(1, 1))