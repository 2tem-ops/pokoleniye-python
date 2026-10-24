# (Не) Активное похудение

number, weight = int(input()), float(input())
goal_weight = 100 - number * 0.2

if weight > goal_weight:
    phrase = "Что-то пошло не так"
else:
    phrase = "Все идет по плану"

print(
    phrase,
    f"#{number} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal_weight} кг",
    sep="\n"
)