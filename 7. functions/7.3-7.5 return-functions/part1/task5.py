# Делители 1

def get_factors(num: int) -> list:
    return [i for i in range(1, num + 1) if num % i == 0]

print(get_factors(1))
print(get_factors(5))
print(get_factors(10))