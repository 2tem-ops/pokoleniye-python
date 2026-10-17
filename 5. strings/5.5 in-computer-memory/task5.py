# Стоимость ответа

text = input()
total = 0

for c in text:
    total += ord(c)

print(f"Текст сообщения: '{text}'",
      f"Стоимость сообщения: {total * 3}🐝",
      sep="\n"
      )