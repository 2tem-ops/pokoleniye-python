# Количество членов

counter = 0
word = input()

while word != "стоп" and word != "хватит" and word != "достаточно":
    counter += 1
    word = input()

print(counter)