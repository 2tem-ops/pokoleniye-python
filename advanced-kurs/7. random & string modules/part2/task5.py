# Тайный друг

from random import choice

def get_secret_friend(students: tuple[str]) -> dict[str, str]:
    frds = {}
    studs = list(students)
    for k in students:
        j = choice(studs)
        while k == j:
            j = choice(studs)
        frds[k] = studs.pop(studs.index(j))
    return frds


students = ('Светлана', 'Аркадий', 'Борис')
print(get_secret_friend(students))

