# Next Prime

def is_prime(num: int) -> bool:
    divide = [i for i in range(1, num + 1) if num % i == 0]
    return len(divide) == 2 and (1 in divide and num in divide)

def get_next_prime(num: int) -> int:
    while not is_prime(num + 1):
        num += 1
    return num + 1



print(get_next_prime(97))
print(get_next_prime(2))
print(get_next_prime(14))
