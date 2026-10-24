# Роскомнадзор запретил букву а

word = input() + " запретил букву"

letters = sorted(set(word.replace(" ", "")))

for letter in letters:
    print(word, letter)
    word = " ".join(word.replace(letter, "").split())

