numbers = [1, 6, 18]

print({num: [i for i in range(1, num // 2 + 1) if num % i == 0] + [num] for num in numbers})