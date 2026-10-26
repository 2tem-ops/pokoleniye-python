# Счетчик верных решений

from math import floor, ceil

n = int(input())

unique_correct = set()
total_correct = 0

def math_round(value: float) -> int:
    work = str(value)
    decimal_point = work.find(".") + 1
    if int(work[decimal_point]) >= 5:
        return ceil(value)
    else:
        return floor(value)

for _ in range(n):
    s = input().split(":")

    name = s[0]
    grade = s[1].lstrip()

    if grade == "Correct":
        total_correct += 1
        unique_correct.add(name)

if total_correct != 0:
    print(f"Верно решили {len(unique_correct)} учащихся")
    print(f"Из всех попыток {math_round((total_correct / n) * 100)}% верных")
else:
    print("Вы можете стать первым, кто решит эту задачу")