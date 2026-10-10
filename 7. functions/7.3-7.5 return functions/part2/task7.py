# Good password

def is_password_good(password: str) -> bool:
    uppers, lowers, digits = 0, 0, 0
    for char in password:
        if char.isupper() and char.isalpha():
            uppers += 1
        elif char.islower() and char.isalpha():
            lowers += 1
        elif char.isdigit():
            digits += 1

    return len(password) >= 8 and uppers >= 1 and lowers >= 1 and digits >= 1

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

