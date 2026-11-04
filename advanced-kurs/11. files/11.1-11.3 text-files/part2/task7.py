# Имя + фамилия

from random import choice

def generate_name(name_file: str, surname_file: str) -> str:
    with open(name_file, "r", encoding="utf-8") as names, open(surname_file, "r", encoding="utf-8") as surnames:
        return f"{choice(names.readlines()).strip()} {choice(surnames.readlines()).strip()}"

print(generate_name('first_names1.txt', 'last_names1.txt'))