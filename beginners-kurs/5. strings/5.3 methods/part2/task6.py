# Самый частотный символ

s = input()
maximum = 0
letter = ""

for i in range(len(s)):
    if s.count(s[i]) >= maximum:
        maximum = s.count(s[i])
        letter = s[i]


print(letter)