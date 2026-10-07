# Шифр Цезаря

n, caesar = int(input()), input()
decoded = ""

for c in caesar:
    if ord(c) - n < 97:
        diff = 97 - (ord(c) - n)
        decoded += chr(123 - diff)
    else:
        decoded += chr(ord(c) - n)

print(decoded)