# Сортируй как хочешь

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

sorting = (
    lambda x: x[0],
    lambda x: x[1],
    lambda x: x[2],
    lambda x: x[3]
)

print(*(" ".join(map(str, athlete)) for athlete in sorted(athletes, key=sorting[int(input()) - 1])), sep="\n")
