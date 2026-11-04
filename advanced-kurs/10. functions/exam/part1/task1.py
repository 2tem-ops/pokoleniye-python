# Письмо для экзамена

def generate_letter(mail: str, name: str, date: str, time: str, place: str, teacher: str="Тимур Гуев", number: int=17):
    return f'''To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}.
Экзамен будет проводить {teacher} в кабинете {number}.
Желаем удачи на экзамене!'''

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))