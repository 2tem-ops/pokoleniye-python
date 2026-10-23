# Аве, Цезарь

caesar = input().split()

def caesar_cipher(word: str) -> str:
    encoded = ""
    n = len(word.strip(',.!?"'))

    for c in word:
        if c.isalpha():
            if c.lower() == c:
                if ord(c) + n > 122:
                    diff = (ord(c) + n) - 123
                    encoded += chr(97 + diff)
                else:
                    encoded += chr(ord(c) + n)

            elif c.upper() == c:
                if ord(c) + n > 90:
                    diff = (ord(c) + n) - 91
                    encoded += chr(65 + diff)
                else:
                    encoded += chr(ord(c) + n)
        else:
            encoded += c

    return encoded

res = []
for w in caesar:
    res.append(caesar_cipher(w))
print(" ".join(res))
