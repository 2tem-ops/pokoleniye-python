from random import randint

def coin_flip():
    return ("Орел", "Решка")[randint(0, 1)]

print(coin_flip())
