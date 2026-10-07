# Строковые минимум и максимум

maximum = ""
minimum = "я"

while True:
    word = input()
    if word == "КОНЕЦ":
        break
    else:
        if word > maximum:
            maximum = word
        if word < minimum:
            minimum = word

print(f"Минимальная строка ⬇️: {minimum}",
      f"Максимальная строка ⬆️: {maximum}",
      sep="\n"
      )
