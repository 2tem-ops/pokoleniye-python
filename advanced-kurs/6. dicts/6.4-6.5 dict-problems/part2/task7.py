# Функция scrabble()

from collections import Counter

def scrabble(letters: str, word: str) -> bool:
    data_1 = Counter(word.lower())
    data_2 = Counter(letters.lower())
    return data_1 & data_2 == data_1

print(scrabble('ABCDEF', 'abcde'))