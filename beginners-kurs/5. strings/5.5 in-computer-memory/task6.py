# Накручиваем стоимость ответа

english = "eyopaxcETOPAHXCBM"
russian = "еуорахсЕТОРАНХСВМ"

word = input()
old_total = 0
new_total = 0

for c in word:
    old_total += ord(c)

for c in word:
    if c in english:
        word = word.replace(c, russian[english.index(c)])

for c in word:
    new_total += ord(c)

print(f"Старая стоимость: {old_total * 3}🐝",
      f"Новая стоимость: {new_total * 3}🐝",
      sep="\n"
      )