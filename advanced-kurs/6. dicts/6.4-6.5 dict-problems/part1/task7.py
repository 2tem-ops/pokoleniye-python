# Секретное слово

secret = input()
data = {}

for _ in range(int(input())):
    s = input().split(": ")
    data[int(s[1])] = s[0]

res = set()

for key in data:
    for char in secret:
        if secret.count(char) == key:
            res.add((key, char))

output = ""

for char in secret:
    for pair in res:
        if pair[1] == char:
            output += data[pair[0]]

print(output)
