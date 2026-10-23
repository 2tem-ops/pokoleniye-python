from random import shuffle, choice
from string import punctuation, digits, ascii_uppercase, ascii_lowercase

def char_list(temp: str):
    dig = input("Включать цифры от 0-9? (д/н) ")
    up = input("Включать прописные буквы? (д/н) ")
    low = input("Включать строчные буквы? (д/н) ")
    symb = input("Включать символы? (д/н) ")
    uncert = input("Исключать неоднозначные символы (il1Lo0O)? (д/н) ")

    if dig == "д": temp += digits
    if up == "д": temp += ascii_uppercase
    if low == "д": temp += ascii_lowercase
    if symb == "д": temp += punctuation
    if uncert == "д": temp = "".join([i for i in temp if i not in "il1Lo0O"])

    return temp

def generate_password(length: int, acceptable: str):
    password = []
    while len(password) != length:
        password.append(choice(acceptable))
        shuffle(password)
    return "".join(password)

def main():
    amount = int(input("Количество паролей: "))
    length = int(input("Длина одного пароля: "))

    acceptable = char_list("")

    for _ in range(amount):
        print(generate_password(length, acceptable))

if __name__ == "__main__":
    main()