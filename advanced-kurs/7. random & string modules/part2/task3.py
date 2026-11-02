from random import shuffle

def get_anagram(word: str) -> str:
    word = list(word)
    shuffle(word)
    return "".join(word)

print(get_anagram('топорик'))