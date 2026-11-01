# Словарь синонимов

synonyms = {}

for _ in range(int(input())):
    pair = input().split()
    synonyms[pair[0]] = pair[1]

find = input()

found = sum([k for k in synonyms.items() if find in k], start=())
print(*[i for i in found if i != find])