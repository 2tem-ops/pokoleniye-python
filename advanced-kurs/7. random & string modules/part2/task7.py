# Генератор паролей 2

from string import ascii_lowercase, ascii_uppercase, digits
from random import choice

def generate_password(length: int) -> str:
    exclude = "lI1oO0"
    password = "" + choice([i for i in set(ascii_uppercase) if i not in exclude]) + choice([i for i in set(digits) if i not in exclude]) + choice([i for i in set(ascii_lowercase) if i not in exclude])
    while len(password) < length:
        password += choice([i for i in set(ascii_lowercase + ascii_uppercase + digits) if i not in exclude])
    return password

def generate_passwords(count: int, length: int) -> list[str]:
    return [generate_password(length) for _ in range(count)]

print(*generate_passwords(int(input()), int(input())), sep="\n")

