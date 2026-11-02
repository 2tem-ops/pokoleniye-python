# Генератор паролей 1

from string import ascii_lowercase, ascii_uppercase, digits
from random import choice

def generate_password(length: int) -> str:
    exclude = "lI1oO0"
    return "".join(choice([i for i in ascii_lowercase + ascii_uppercase + digits if i not in exclude]) for _ in range(length))

def generate_passwords(count: int, length: int) -> list[str]:
    return [generate_password(length) for i in range(count)]

print(*generate_passwords(int(input()), int(input())), sep="\n")