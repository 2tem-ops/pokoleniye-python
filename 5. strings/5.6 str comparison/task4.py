# Сортируем слова

word1, word2, word3 = input(), input(), input()

if word1 > word2 > word3:
    maximum = word1
    minimum = word3
if word1 > word3 > word2:
    maximum = word1
    minimum = word2
if word2 > word1 > word3:
    maximum = word2
    minimum = word3
if word2 > word3 > word1:
    maximum = word2
    minimum = word1
if word3 > word2 > word1:
    maximum = word3
    minimum = word1
if word3 > word1 > word2:
    maximum = word3
    minimum = word2

if (word1 == maximum and word3 == minimum) or (word1 == minimum and word3 == maximum):
    middle = word2
elif (word2 == maximum and word3 == minimum) or (word2 == minimum and word3 == maximum):
    middle = word1
elif (word2 == maximum and word1 == minimum) or (word2 == minimum and word1 == maximum):
    middle = word3

print(minimum, middle, maximum)
