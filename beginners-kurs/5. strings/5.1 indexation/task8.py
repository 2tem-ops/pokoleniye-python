# Одинаковые соседи

s = input()
pairs = 0

for i in range(len(s)):
    if i != len(s) - 1:
        if s[i] == s[i + 1]:
            pairs += 1

print(pairs)