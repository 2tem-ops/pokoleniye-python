# Волшебное число

word1, word2, word3, word4 = input(), input(), input(), input()

maximum = max(word1, word2, word3, word4)
minimum = min(word1, word2, word3, word4)

result = (ord(minimum[-1]) * ord(maximum[-1])) ** 2
print(result)

