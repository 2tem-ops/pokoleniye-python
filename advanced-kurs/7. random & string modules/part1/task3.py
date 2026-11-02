from string import ascii_lowercase, ascii_uppercase
from random import choice

def generate_password(length: int) -> str:
    return "".join(choice(ascii_lowercase + ascii_uppercase) for _ in range(length))

print(generate_password(7))
print(generate_password(10))
print(generate_password(6))
print(generate_password(8))