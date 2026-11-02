# Порядковый номер

text = input().split()
data = {}

for word in text:
    data[word] = data.get(word, 0) + 1
    print(data[word], end=" ")