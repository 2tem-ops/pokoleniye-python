# Палиндром

def is_palindrome(text: str) -> bool:
    clean = "".join(i.lower() for i in text if i.isalnum())
    return clean == clean[::-1]

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))