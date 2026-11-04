# Гематрия слова

words = []

for _ in range(int(input())): words.append(input())

def sum_ords(word: str) -> tuple[int, str]:
    return sum(ord(char) - 65 for char in word.upper()), word

print(*sorted(words, key=sum_ords), sep="\n")