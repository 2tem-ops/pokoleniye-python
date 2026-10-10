# Is the Number Prime?

def is_prime(num: int) -> bool:
    divide = [i for i in range(1, num + 1) if num % i == 0]
    return len(divide) == 2 and (1 in divide and num in divide)

print(is_prime(16))