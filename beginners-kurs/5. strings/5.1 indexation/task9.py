# Гласные и согласные

s = input()

vowels = "ауоыиэяюе"
consonants = "бвгджзйклмнпрстфхцчшщ"

vowel = 0
consonant = 0

for c in s:
    if c.lower() in vowels:
        vowel += 1
    elif c.lower() in consonants:
        consonant += 1

print(f"Количество гласных букв равно {vowel}",
      f"Количество согласных букв равно {consonant}",
      sep="\n")