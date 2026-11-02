favorite_numbers = {
    'scarlett': 41, 'den': 22, 'viktor': 321, 'lera': 777, 'mahad': 4,
    'manny': 4, 'ken': 8423, 'borya': 12
}

print({k: v for k, v in favorite_numbers.items() if 10 <= v <= 99})