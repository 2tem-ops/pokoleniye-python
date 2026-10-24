# Нижний регистр

s = input()
counter = 0

for c in s:
    if c != c.upper():
        counter += 1

print(counter)