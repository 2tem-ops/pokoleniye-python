# Делители 2

def number_of_factors(num: int) -> int:
    return len([i for i in range(1, num + 1) if num % i == 0])

print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))