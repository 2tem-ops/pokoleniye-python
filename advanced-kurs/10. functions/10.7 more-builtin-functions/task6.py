# Хороший пароль

password = input()

print("YES" if all([len(password) >= 7, [char for char in password if char.isdigit()], [char for char in password if char.isupper()], [char for char in password if char.islower()]]) else "NO")