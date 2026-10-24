# Искомый месяц

def get_month(language: str, number: int) -> str | None:
    lng_ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
    lng_en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']
    if language == "ru":
        return lng_ru[number]
    elif language == "en":
        return lng_en[number]
    else:
        return None

print(get_month('ru', 1))
print(get_month('ru', 12))
print(get_month('en', 1))
print(get_month('en', 10))