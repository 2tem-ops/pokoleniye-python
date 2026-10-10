# BEEGEEK

def is_palindrome(text: str) -> bool:
    return text == text[::-1]

def is_prime(num: int) -> bool:
    divide = [i for i in range(1, num + 1) if num % i == 0]
    return len(divide) == 2 and 1 in divide and num in divide

def  is_even(num: int) -> bool:
    return num % 2 == 0

def is_valid_password(password: str) -> bool:
    password = [int(i) for i in password.split(":")]
    return len(password) == 3 and is_palindrome(str(password[0])) and is_prime(password[1]) and is_even(password[2])

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))