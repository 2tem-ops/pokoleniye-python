# Случайная строка

from random import choice

def get_random_string(filename: str) -> str:
    try:
        file = open(filename, 'r', encoding='utf-8')
        return choice(file.readlines()).rstrip()
    except FileNotFoundError:
        return ''
    else:
        file.close()