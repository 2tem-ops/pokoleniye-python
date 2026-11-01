# Самое редкое слово

text = [i.lower().strip(".,!?:;-") for i in input().split()]
print(min(text, key=lambda word: (text.count(word), word)))