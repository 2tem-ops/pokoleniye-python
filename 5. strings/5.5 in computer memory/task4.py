# Самое тяжёлое слово

max_heaviness = 0

for i in range(4):
    word = input()
    cur_heaviness = 0

    for c in word:
        cur_heaviness += ord(c)

    if cur_heaviness > max_heaviness:
        max_heaviness = cur_heaviness
        heaviest_word = word

print(heaviest_word)




