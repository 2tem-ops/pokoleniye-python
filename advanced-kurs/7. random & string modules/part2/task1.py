from random import randint

def generate_ip_address() -> str:
    return f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"

print(generate_ip_address())
print(generate_ip_address())
print(generate_ip_address())
print(generate_ip_address())