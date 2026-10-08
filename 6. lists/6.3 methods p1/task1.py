# Алфавит

alphabet = "abcdefghijklmnopqrstuvwxyz"

lst = []

for i in alphabet:
    lst.append(i * (alphabet.index(i) + 1))

print(lst)