# ФИО

def print_fio(name: str, surname: str, patronymic: str):
    print(surname.upper()[0] + name.upper()[0] + patronymic.upper()[0])

print_fio(input(), input(), input())