# Количество слов в тексте
import string

print(len(set(input().lower().translate(str.maketrans('', '', string.punctuation)).split())))